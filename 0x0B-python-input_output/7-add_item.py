#!/usr/bin/python3
"""This is a python module"""


import sys
"""system module"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
if __name__ == "__main__":
    file = "add_item.json"
    argv = sys.argv
    del argv[0]
    try:
        obj = load_from_json_file(file)
    except:
        obj = []
    obj = obj + argv
    save_to_json_file(obj, file)
