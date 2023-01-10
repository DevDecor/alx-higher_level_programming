#!/usr/bin/python3
"""Python module"""


def read_file(filename=""):
    """Prints file content"""
    with open(filename) as f:
        print(f.read())
