#!/usr/bin/python3
"""In this code we are going to create the class called Plaza and show an
error if it is not int"""


class Square:
    """This class instance size"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        Area = self.size ** 2
        return Area

    def my_print(self):
        if self.size == 0:
            print('')
        for i in range(self.size):
            print(self.size * '#')
