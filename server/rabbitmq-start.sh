#!/bin/bash

if [[ ${UID} -ne 0 ]]; then
	echo "Run as root"
	exit 0
fi

rabbitmq-server -detached
