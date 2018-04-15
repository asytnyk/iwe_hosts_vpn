#!/bin/bash

cd $HOME/dev/iwe_hosts_vpn
docker build -t iwe_hosts_vpn:latest . -f docker/Dockerfile 
