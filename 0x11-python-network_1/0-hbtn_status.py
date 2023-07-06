#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request
url = ''
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    res = response.read()
    temp = f"""Body response:
\t- type: {type(res)}
\t- content: {res}
\t- utf8 content: {str(res, 'utf-8')}"""
    print(temp)