#!/usr/bin/python3
"""
 function that writes an Object to a text file,
 using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file
    """

    import json
    ej = json.dumps(my_obj)
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(ej)
