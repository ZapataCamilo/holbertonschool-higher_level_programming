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

    @staticmethod
    def to_json_string(list_dictionaries):
        "that returns the JSON string representation of list_dictionaries"
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        lis = []
        if list_objs is None:
            list_objs = []
        for i in list_objs:
            lis.append(i.to_dictionary())
        with open(f'{cls.__name__}.json', mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(lis))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return json_string == []
        return json.loads(json_string)
