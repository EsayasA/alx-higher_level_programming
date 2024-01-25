#!/bin/bash
# script takes URL and send requist then  displays
# size of the response body
# size in byte
# use curl
# script takes URL and send requist then  displays
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
