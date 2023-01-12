#!/usr/bin/python3
"""Python module"""
import json
"""Python json module"""


def load_from_json_file(filename):
    """Prints file content"""
    with open(filename, 'r') as f:
        content = f.read()
        x = []
        try:
            x = json.loads(content)
        except:
            return []
    return x
