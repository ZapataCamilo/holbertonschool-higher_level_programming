#!/usr/bin/python3

def islower(c):

    convert = ord(c)
    for i in range(97, 122):
        if convert == i:
            return True
        else:
            return False
