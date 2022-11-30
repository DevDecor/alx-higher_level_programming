#!/usr/bin/python3
def uppercase(s):
    b = ""
    for i in range(0, len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            b = b + "{:c}".format(ord(s[i]) - 32)
            continue
        b = b + s[i]
    print(b)
