#!/usr/bin/python3
"""
Write a class BaseGeometry
"""


class BaseGeometry:
    """
    raises an Exception, TypeError and TypeError
    with the message area() is not implemented
    """

    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise ValueError ('{} must be greater than 0'.format(self.name))

class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from 
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
