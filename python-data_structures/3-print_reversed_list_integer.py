#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if not my_list:
        return
    for i in range(len(my_list)):
        i += 1
        print('{:d}'.format(my_list[-i]))
