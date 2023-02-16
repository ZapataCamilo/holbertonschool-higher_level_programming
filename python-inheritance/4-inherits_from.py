#!/usr/bin/python3
"""returns True if the object is an instance of a class that
inherited (directly or indirectly)
from the specified class"""


def inherits_from(obj, a_class):
    """Checks if the object is an  instance of a class that inherited"""
    
    if isinstance(obj, a_class):
        obj = int()
        return isinstance(obj, a_class)
    else:
        return False
