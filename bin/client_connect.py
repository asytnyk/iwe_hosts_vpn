#!/usr/local/bin/venv/bin/python3
''' Check if client with this CommonName should be allowed to connect '''

import errno
import os
import sys
import requests
import simplejson as json

def main():
    ''' good old main '''

    environ = os.environ
    if not 'common_name' in environ.keys():
        print('Where are the environment variables?')
        sys.exit(errno.EACCES)

    conf = json.load(open('/etc/client_connect.json'))
    if not conf:
        print('Where is the configuration file?')
        sys.exit(errno.EACCES)

    client_connect_url = conf['client_connect_url']
    client_connect_secret = conf['client_connect_secret']

    common_name = environ['common_name']
    envdict = {}
    for key in environ.keys():
        envdict[key] = environ[key]

    try:
        client_connect = requests.post(
            '{}/{}'.format(client_connect_url, common_name),
            headers={'secret-key': client_connect_secret},
            json=envdict)
    except:
        print('Something wrong when asking iWegard about {}. Got an exception on requests.post(...)'.format(common_name))
        sys.exit(errno.EACCES)

    if client_connect.status_code != 200:
        print('Something wrong when asking iWegard about {}. status_code = {}'.format(common_name, client_connect.status_code))
        sys.exit(errno.EACCES)

    client_connect_json = client_connect.json()

    if client_connect_json['uuid'] == common_name \
       and client_connect_json['vpn-name'] == 'hosts' \
       and client_connect_json['allow-connection'] == 'True':
        print('iWegard says that {} is good to connect'.format(common_name))
        sys.exit(0)

    print('iWegard says that {} is NOT good to connect'.format(common_name))
    sys.exit(errno.EPERM)


if __name__ == "__main__":
    main()
