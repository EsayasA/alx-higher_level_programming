#!/usr/bin/python3
"""Sends a request to URL."""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    ask = requests.get(url)
    if ask.status_code >= 400:
        print("Error code: {}".format(ask.status_code))
    else:
        print(ask.text)
