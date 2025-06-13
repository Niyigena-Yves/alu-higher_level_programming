#!/usr/bin/python3
""" A script that:
- takes a URL as input,
- sends a request to that URL, and retrieves the value
- of the X-Request-Id header from the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
