#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    """Fires a get request"""
    print(dict(response.info())['X-Request-Id'])
