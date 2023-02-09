#!/usr/bin/python3
"""This function is to add two integers"""


def add_integer(a, b=98):
    """Adds two integers"""
    """
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == '__main__':
    import doctest
    doctest.testfile
