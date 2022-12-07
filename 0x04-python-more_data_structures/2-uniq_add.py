#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    for i in list(set(my_list)):
        add = add + i
    return add
