#!/usr/bin/python3
"""
function that returns the dictionary description with simple data
structurefor JSON serialization of an object:
"""


def class_to_json(obj):
    """
    Return the dict object.
    """
    return obj.__dic__
