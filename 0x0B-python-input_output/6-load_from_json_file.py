#!/usr/bin/python3
"""Python module"""
import json
"""Python json module"""


def load_from_json_file(filename):
    """Prints file content"""
    with open(filename, 'w') as f:
        x = json.loads(f)
    f.close()
    return x
