#!/usr/bin/env python3

env = {"script_type": "client-connect", "time_unix": "1523695124",
"time_ascii": "Sat Apr 14 08:38:44 2018", "ifconfig_pool_netmask":
"255.255.255.0", "ifconfig_pool_remote_ip": "10.8.0.2", "trusted_port":
"44528", "trusted_ip": "172.17.0.1", "common_name":
"d185fcd851994c6fa32957179b608e34", "untrusted_port": "44528",
"untrusted_ip": "172.17.0.1", "tls_serial_hex_0":
"6e:27:c3:b5:46:8c:92:44:11:aa:4b:21:3c:8d:08:00", "tls_serial_0":
"146421548545827622477907451459584985088", "tls_digest_0":
"37:44:e1:f3:6d:b2:f4:3e:e8:be:58:a7:33:60:25:fc:94:7b:49:8b",
"tls_id_0": "CN=d185fcd851994c6fa32957179b608e34", "X509_0_CN":
"d185fcd851994c6fa32957179b608e34", "tls_serial_hex_1":
"f0:cd:f7:69:10:86:db:ec", "tls_serial_1": "17351796969949289452",
"tls_digest_1":
"a0:6e:f4:e1:c4:71:c6:b2:84:e4:de:3c:df:ab:50:c7:2a:0a:b9:19",
"tls_id_1": "CN=ca.beta.iwe.cloud", "X509_1_CN": "ca.beta.iwe.cloud",
"remote_port_1": "1194", "local_port_1": "1194", "proto_1": "udp",
"daemon_pid": "48", "daemon_start_time": "1523695116",
"daemon_log_redirect": "0", "daemon": "0", "verb": "3", "config":
"/etc/openvpn/conf/server/hosts-vpn.conf", "ifconfig_local": "10.8.0.1",
"ifconfig_netmask": "255.255.255.0", "ifconfig_broadcast": "10.8.0.255",
"script_context": "init", "tun_mtu": "1500", "link_mtu": "1557", "dev":
"tun0", "dev_type": "tun", "redirect_gateway": "0"}

def main():
    for key in env.keys():
        print ('export {}="{}"; '.format(key, env[key]), end='')
    print(' ')

if __name__ == "__main__":
    main()
