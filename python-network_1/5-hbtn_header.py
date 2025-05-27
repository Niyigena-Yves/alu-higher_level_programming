#!/usr/bin/python3
""" Fetches and displays the X-Request-Id header from a request. """
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
