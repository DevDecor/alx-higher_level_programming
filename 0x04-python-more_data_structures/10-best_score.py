#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    m = a_dictionary.values()[0]
    best = ""
    for i in a_dictionary:
        if a_dictionary[i] > m:
            m = a_dictionary[i]
            best = i
    return i
