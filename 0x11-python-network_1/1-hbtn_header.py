#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL"""

from sys import argv
from urllib.request import Request, urlopen


if __name__ == "__main__":
    ask = Request(argv[1])

    with urlopen(ask) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
