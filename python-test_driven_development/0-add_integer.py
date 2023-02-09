#!/usr/bin/python3
def add_integer(a, b=98):
    """
        >>> add_integer(10, 10)
        20
        >>> add_integer(14, 30)
        44
        >>> add_integer(int(10.0), int(20.0))
        30
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
