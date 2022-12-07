def print_sorted_dictionary(a_dictionary):
    new = {}
    for i in sorted(a_dictionary.keys()):
        new[i] = a_dictionary[i]
    return new
