#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """raises an Exception, TypeError and TypeError
    with the message area() is not implemented"""

    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if value <= 0:
            raise TypeError('{} must be greater than 0'.format(self.name))
