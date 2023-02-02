#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for x in a_dictionary:
        b_dictionary[x] *= 2
    return b_dictionary
