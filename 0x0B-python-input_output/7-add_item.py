#!/usr/bin/python3
"""This is a python module"""


import sys
"""system module"""

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
if __name__ == "__main__":
    file = "add_item.json"
    with open(file, "r+") as f:
        if not f.read():
            f.write('[]')
        f.close()
    argv = sys.argv
    del argv[0]
    obj = load_from_json_file(file)
    obj = obj + argv
    save_to_json_file(obj, file)
