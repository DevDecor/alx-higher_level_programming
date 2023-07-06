#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request
import sys

with request.urlopen(sys.argv[1]) as response:
    """Fires a get request"""
    res = dict(response.info())['X-Request-Id']
    # [x for x in response.info().split('\n') if 'X-Request-Id' in x][0]
    print(res)
