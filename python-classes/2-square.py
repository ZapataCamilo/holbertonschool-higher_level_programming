#!/usr/bin/python3
"""In this code we are going to create the class called Plaza and show an
error if it is not int"""


class Square:
    """This class instance size"""

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
