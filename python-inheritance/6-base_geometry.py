#!/usr/bin/python3
"""Write a class BaseGeometry"""


class BaseGeometry:
    """raises an Exception with the message area() is not implemented"""

    def __init__(self) -> None:
        pass

    def area(self):
        raise Exception('area() is not implemented')
