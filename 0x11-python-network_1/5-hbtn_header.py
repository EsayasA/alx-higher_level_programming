#!/usr/bin/python3
"""Displays the X-Request-Id header"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    ask = requests.get(url)
    print(ask.headers.get("X-Request-Id"))