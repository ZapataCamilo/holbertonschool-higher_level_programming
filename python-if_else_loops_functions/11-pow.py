#!/usr/bin/python3
def pow(a, b):
    result = a ** b
    if result < 0:
        result = a ** -b
        return(result)
    return(result)
