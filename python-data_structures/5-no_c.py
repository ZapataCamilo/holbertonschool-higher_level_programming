#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for no_letter in my_string:
        if no_letter == 'c' or no_letter == 'C':
            no_letter = ''
        new_str += no_letter
    return new_str
