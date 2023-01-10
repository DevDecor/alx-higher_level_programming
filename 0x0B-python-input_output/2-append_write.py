#!/usr/bin/python3
"""Python module"""


def append_write(filename="", text=""):
    """Prints file content"""
    with open(filename, 'a') as f:
        x = f.write(text)
    f.close()
    return x
