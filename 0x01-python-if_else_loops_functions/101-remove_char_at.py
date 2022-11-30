#!/usr/bin/python3
def remove_char_at(s, n):
    x = ''
    for i in range(0, len(s) + 1):
        if i != n:
            x = x + s[i]
    return x
