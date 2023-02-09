#!/usr/bin/python3
"""print a square"""


def print_square(size):
    """This function is to print s square with #"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
