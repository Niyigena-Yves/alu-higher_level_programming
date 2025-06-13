#!/usr/bin/python3
""" A script that:
- accepts a URL as an argument,
- sends a request to that URL,
- and prints the body of the response (decoded in UTF-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
