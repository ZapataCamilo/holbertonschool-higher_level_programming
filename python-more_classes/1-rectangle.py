#!/usr/bin/python3
"""In this code we are going to create a class call Rectangle"""


class Rectangle:
    """Rectangle is the class wiht width and height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return_width = self.__width
        return return_width
    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
         
         if not isinstance(value, int):
             raise TypeError('height must be an integer')
         if value < 0:
             raise ValueError('height must be >= 0')
         self.__height = value
