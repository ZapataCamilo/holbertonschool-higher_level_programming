#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length:
        return length, sentence[0]
    elif not length:
        return length, None
