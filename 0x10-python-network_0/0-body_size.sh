#!/bin/bash
# script take and send url, and displays
# the size body of the response.
# The size in bytes
# You use curl
# script that takes , sends a request to that URl and display.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
