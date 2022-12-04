#!/usr/bin/python3
def no_c(my_string):
    x = ""
    for i in range(len(my_string)):
        if ord(my_string[i]) == ord("c") or ord(my_string[i]) == ord("C"):
            continue
        x = x + my_string[i]
    return x
