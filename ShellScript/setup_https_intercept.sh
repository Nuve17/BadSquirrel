#!/bin/sh
rm -rf certs
apt-get install dnsmasq -y
cp -f local.conf /etc/dnsmasq.d/
openssl genrsa -out ca.key 2048
openssl req -new -nodes -x509 -days 3650 -key ca.key -out ca.crt -subj "/CN=BadSquirrel CA"
openssl genrsa -out cert.key 2048
mkdir certs/
