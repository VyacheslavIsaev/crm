#!/bin/bash

# Creates SSL certificate and private key
# The key.pem and cert.pem outputs are stored in the TARGET directory.

export TARGET=./certs
mkdir -p $TARGET
openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 \
    -subj "/C=SI/ST=SI/L=Ljubljana/O=Nil/CN=crm.nil.com" \
    -keyout $TARGET/key.pem -out $TARGET/cert.pem
