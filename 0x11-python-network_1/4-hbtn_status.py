#!/usr/bin/python3
"""Fetches the URL:Python script that fetches 
https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    gi = requests.get('https://intranet.hbtn.io/status')

    print('Body response:')
    print('\t- type: {_type}'.format(_type=type(gi.text)))
    print('\t- content: {_content}'.format(_content=gi.text))
