#!/bin/bash

if [ $# -lt "2" ] ;then
    echo "Paramters are required!"
    exit 1
fi

echo "Waiting for the following URL come to live"
echo $2

COUNT=$1

while ! curl --output /dev/null --silent --head --fail --insecure $2 && [ $COUNT -gt "0" ]; do
    sleep 1
    echo -n "."
    let COUNT=$COUNT-1
done

if curl --output /dev/null --silent --head --fail --insecure $2; then
    echo "Alive!"
else
    echo "DEAD! SoRRRyy :("
    exit 1
fi
