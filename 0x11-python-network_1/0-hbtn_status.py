#!/usr/bin/python3
# Fetches https://alx-intranet.hbtn.io/status

import urllib.request as request
url = 'https://alx-intranet.hbtn.io/status'
with request.urlopen(url) as res:
    temp = f"""Body response:
\t- type: {type(res.read())}
\t- content: {res.read()}
\t- utf8 content: {str(res.read(), 'utf-8')}"""
    print(temp)