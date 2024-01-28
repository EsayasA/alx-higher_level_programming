#!/usr/bin/python3
"""You must use the GitHub API, here is the documentation 
https://developer.github.com/v3/repos/commits/."""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    result = req.json()
    try:
        for k in range(10):
            print("{}: {}".format(
                result[k].get("sha"),
                result[k].get("commit").get("author").get("name")))
    except IndexError:
        pass
