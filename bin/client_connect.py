#!/usr/bin/env python3
''' Check if client with this CommonName should be allowed to connect '''

import errno
import os
import sys
import requests

VPN_CLIENT_CONNECT_URL = os.environ.get('VPN_CLIENT_CONNECT_URL') \
    or 'https://beta.iwe.cloud/backend/vpn/hosts/client-connect'

VPN_CLIENT_CONNECT_SECRET_KEY = os.environ.get('VPN_CLIENT_CONNECT_SECRET_KEY') \
    or 'Su6oLpYQv5whthmNrjtf'

def main():
    ''' good old main '''

    environ = os.environ
    if not 'common_name' in environ.keys():
        print('Where are the environment variables?')
        sys.exit(-errno.EACCES)

    common_name = environ['common_name']

    try:
        client_connect = requests.post(
            '{}/{}'.format(VPN_CLIENT_CONNECT_URL, common_name),
            headers={'secret-key': VPN_CLIENT_CONNECT_SECRET_KEY},
            data=environ)
    except:
        print('Something wrong when asking iWegard about {}'.format(common_name))
        sys.exit(-errno.EACCES)

    client_connect_json = client_connect.json()

    if client_connect_json['uuid'] == common_name \
       and client_connect_json['vpn-name'] == 'hosts' \
       and client_connect_json['allow-connection'] == 'True':
        sys.exit(0)

    sys.exit(-errno.EPERM)


if __name__ == "__main__":
    main()
