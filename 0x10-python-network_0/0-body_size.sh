#!/bin/bash
# script take and send url, and displays
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
