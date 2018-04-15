#!/bin/bash

VPN_CLIENT_CONNECT_SECRET_KEY=BF9guWTBFEyrUKX2Go6twtQt

docker run \
	-d \
	--name iwe_hosts_vpn \
	--restart unless-stopped \
	-e VPN_CLIENT_CONNECT_SECRET_KEY=$VPN_CLIENT_CONNECT_SECRET_KEY \
	-p 1194:1194/udp \
	--cap-add=NET_ADMIN \
	iwe_hosts_vpn:latest
