#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if ord(i) >= 97 and ord(i) <= 122:
            print("{:c}".format(ord(i) - 32), end='')
            continue
        print(i, end='')
