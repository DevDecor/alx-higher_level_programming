#!/usr/bin/python3
import sys
av = sys.argv[1:]
ac = len(av)
if __name__ == "__main__":
    x = "s" if ac != 1 else ""
    y = "." if ac == 0 else ":"
    print("{} argument{}{}".format(ac, x, y))
    for i in range(0, len(av)):
        print("{}: {}".format(i + 1, av[i]))
