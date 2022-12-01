#!/usr/bin/python3
import sys
av = sys.argv[1:]
a = 0
if __name__ == "__main__":
    for i in av:
        a = a + int(i)
    print("{}".format(a))
