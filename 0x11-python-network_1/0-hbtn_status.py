#!/usr/bin/python3
"""Fetches the URL"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    gi = Request('https://intranet.hbtn.io/status')

    with urlopen(gi) as resullt:
        content = result.read()
        utf8_content = content.decode('utf-8')

        print('Body response:')
        print('\t- type: {_type}'.format(_type=type(content)))
        print('\t- content: {_content}'.format(_content=content))
        print('\t- utf8 content: {_utf8_c}'.format(_utf8_c=utf8_content))
