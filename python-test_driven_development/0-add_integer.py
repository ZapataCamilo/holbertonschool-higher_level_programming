#!/usr/bin/python3
def add_integer(a, b=98):
    """
        >>> add_integer(10, 10)
        20
        >>> add_integer(5,0, 5,0)
        10,0
        >>> add_integer('a', 'b')
        'ab'
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
