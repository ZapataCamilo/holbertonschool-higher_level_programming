#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        my_string[i] = ord(my_string[i])
        if my_string[i] == 67 or my_string[i] == 99:
            my_string[i] = chr(my_string[i])
            my_string[i].pop(i)
            return my_string