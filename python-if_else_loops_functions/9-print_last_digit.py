#!/bin/usr/python3
def print_last_digit(number):
    if number >= 0:
        i = number % 10
        print(i, end='')
    else:
        i = -number % 10
        return(i)
    return(i)
