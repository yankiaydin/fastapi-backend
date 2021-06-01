#!/bin/bash

ssh root@167.71.12.65 'rm -r ~/firm-db/FirmDb'
scp -r ../bookstoreAPI root@167.71.12.65:~/firm-db

ssh root@167.71.12.65 'docker stop firm-api'
ssh root@167.71.12.65 'docker rm firm-api'

ssh root@167.71.12.65 'docker build -t firm-build ~/firm-db/FirmDb'
ssh root@167.71.12.65 'docker run -idt -e MODULE_NAME="run" -e PORT="3000" -e PRODUCTION="true" -p 3000:3000 --name=firm-api firm-build'


ssh root@167.71.12.65 'docker stop api-nginx'
ssh root@167.71.12.65 'docker rm api-nginx'

ssh root@167.71.12.65 'docker build -t firm-nginx ~/firm-db/FirmDb/nginx-reverse-proxy'
ssh root@167.71.12.65 'docker run -idt --name=api-nginx -p 80:80 firm-nginx'

