#!/usr/bin/python3
"""
Name: base
---------------
Class name: Base
---------------
"""
import json


class Base:
    """
    this class give us a id for the object
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Here we ask if there are id,
        if not put one with the private class attribute __nb_objects
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        "that returns the JSON string representation of list_dictionaries"
        if list_dictionaries is None:
            list_dictionaries = []
            return list_dictionaries
        else:
            return json.dumps(list_dictionaries)
