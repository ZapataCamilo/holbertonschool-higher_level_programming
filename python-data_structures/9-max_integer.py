#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]

    if not my_list:
        return None
    for i in range(len(my_list)):
        if i > max:
            return my_list[max]
