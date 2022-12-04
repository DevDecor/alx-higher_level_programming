#!/usr/bin/python3
def no_c(my_string):
    x = my_string[:]
    for i in range(len(my_string)):
        if x[i] == "c" or if x[i] == "C":
            del x[i]
    return x
