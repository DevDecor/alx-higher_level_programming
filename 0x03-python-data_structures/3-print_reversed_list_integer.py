#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = my_list[:]
    x.reverse()
    if len(my_list) == 0:
        return
    for i in x:
        print("{:d}".format(i))
