#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = my_list[:]
    x.reverse()
    if len(x) == 0:
        print("")
    for i in x:
        print("{:d}".format(i))
