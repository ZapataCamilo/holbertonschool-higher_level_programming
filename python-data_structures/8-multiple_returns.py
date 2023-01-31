#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_dg = sentence[0]
    if not sentence:
        return None
    return length, first_dg
