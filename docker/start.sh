#!/bin/bash

CLIENT_CONNECT_URL="https://beta.iwe.cloud/backend/vpn/hosts/client-connect/"
CLIENT_CONNECT_SECRET="BF9guWTBFEyrUKX2Go6twtQt"

#       -it --entrypoint /bin/sh \
docker run \
	-d \
	--name iwe_hosts_vpn \
	--restart unless-stopped \
	-e CLIENT_CONNECT_URL=$CLIENT_CONNECT_URL \
	-e CLIENT_CONNECT_SECRET=$CLIENT_CONNECT_SECRET \
	-p 1194:1194/udp \
	--cap-add=NET_ADMIN \
	iwe_hosts_vpn:latest
