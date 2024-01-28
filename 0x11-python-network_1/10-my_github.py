#!/usr/bin/python3
"""Sends a search request for a given string to the Star Wars APi"""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    par = {"search": sys.argv[1]}
    res = requests.get(url, par=par).json()

    print("Number of results: {}".format(res.get("count")))
    [print(req.get("name")) for req in res.get("res")]
