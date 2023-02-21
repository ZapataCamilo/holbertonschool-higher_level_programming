#!/usr/bin/python3
"""
Name: rectangle
---------------
Class name: Rectangle
---------------
"""

from models.base import Base


class Rectangle(Base):
    """
    this class give us a id, width and height
    for the object
    width: An integer representing the width of the rectangle.
    height: An integer representing the height of the rectangle.
    x: An integer representing the x coordinate of the rectangle.
    Default is 0.
    y: An integer representing the y coordinate of the rectangle.
    Default is 0.
    id: An integer representing the unique identifier of the rectangle.
    Default is None.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Here we ask if there are id, width and height
        if not put of id one with the private class attribute __nb_objects
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def public_width(self):
        """Returns the value of the __width attribute"""
        return self.__width

    @public_width.setter
    def public_width(self, value):
        """Sets the value of the __width attribute"""
        self.__width = value

    @property
    def public_height(self):
        """Returns the value of the __width attribute"""
        return self.__height

    @public_height.setter
    def public_height(self, value):
        """Sets the value of the __width attribute"""
        self.__height = value

    @property
    def public_x(self):
        """Returns the value of the __width attribute"""
        return self.__x

    @public_x.setter
    def public_x(self, value):
        """Sets the value of the __width attribute"""
        self.__x = value

    @property
    def public_y(self):
        """Returns the value of the __width attribute"""
        return self.__y

    @public_y.setter
    def public_y(self, value):
        """Sets the value of the __width attribute"""
        self.__y = value
