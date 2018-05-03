#!/bin/sh

if [[ "$CLIENT_CONNECT_URL" == "" ]];then
	echo "Please define CLIENT_CONNECT_URL"
	exit
fi

if [[ "$CLIENT_CONNECT_SECRET" == "" ]];then
	echo "Please define CLIENT_CONNECT_SECRET"
	exit
fi

echo "{\"client_connect_url\": \"$CLIENT_CONNECT_URL\", \"client_connect_secret\": \"$CLIENT_CONNECT_SECRET\"}" > /etc/client_connect.json

mkdir -p /dev/net
if [ ! -c /dev/net/tun ]; then
	mknod /dev/net/tun c 10 200
fi

openvpn /etc/openvpn/conf/server/hosts-vpn.conf
