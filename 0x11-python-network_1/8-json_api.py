#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user"""
import sys
import requests


if __name__ == "__main__":
    mes = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": mes}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        result = req.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get("id"), result.get("name")))
    except ValueError:
        print("Not a valid JSON")
