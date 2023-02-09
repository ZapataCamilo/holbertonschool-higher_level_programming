#!/usr/bin/python3
"""print a square"""

def print_square(size):
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be an integer')
    for i in range(size):
        print('#' * size)
