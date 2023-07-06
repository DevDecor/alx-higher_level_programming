#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    # data = parse.urlencode({"email": sys.argv[2]}).encode('ascii')
    # req = request.Request(sys.argv[1], data=data, method='POST')
    try:
        with request.urlopen(sys.argv[1]) as response:
            """Fires a get request"""
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
