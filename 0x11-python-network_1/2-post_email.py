#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]}).encode('ascii')
    req = request.Request(sys.argv[1], data=data, method='POST')
    with request.urlopen(req) as response:
        """Fires a get request"""
        print(response.read().decode('utf-8'))
