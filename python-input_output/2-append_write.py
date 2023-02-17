#!/usr/bin/pyhton3
"""
function that appends a string at the end of a text file
(UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    appends a string at the end
    """
    
    with open(filename, mode='a', encoding='utf-8') as a:
        return a.write(text)
