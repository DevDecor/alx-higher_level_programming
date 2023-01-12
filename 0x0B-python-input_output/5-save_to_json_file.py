#!/usr/bin/python3
"""Python module"""
import json
"""Python json module"""


def save_to_json_file(my_obj, filename):
    """Prints file content"""
    with open(filename, 'w') as f:
        x = f.write(json.dumps(my_obj))
    return x
