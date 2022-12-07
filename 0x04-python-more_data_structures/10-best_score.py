#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    m = 0
    for i in a_dictionary:
        if a_dictionary[i] > m:
            m = a_dictionary[i]
    return m
