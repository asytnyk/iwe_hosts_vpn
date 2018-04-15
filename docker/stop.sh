#!/bin/bash

containers="iwe_hosts_vpn"

for container in $containers; do
        docker stop $container
done

if [[ "$1" == "--rm" ]];then
	for container in $containers; do
		docker rm $container
	done
fi

