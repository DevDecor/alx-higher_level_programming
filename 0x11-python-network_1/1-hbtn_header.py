#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request
import sys

with request.urlopen(sys.argv[1]) as response:
    """Fires a get request"""
    print(dict(response.info())['X-Request-Id'])
