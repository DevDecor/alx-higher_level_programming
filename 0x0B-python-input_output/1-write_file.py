#!/usr/bin/python3
"""Python module"""


def write_file(filename="", text=""):
    """Prints file content"""
    with open(filename, 'w') as f:
        f.write(text)
