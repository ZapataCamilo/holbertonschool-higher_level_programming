#!/usr/bin/python3

class Base:
    """
    This class is to now if there are a id in the object or not
    """

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
