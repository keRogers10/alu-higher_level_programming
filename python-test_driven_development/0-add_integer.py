#!/usr/bin/python3
"""
testing add_integer to check if it passes all the tests
"""


def add_integer(a, b=98):
    if type(a) != int or type(a) != float:
        raise TypeError('a must be an integer')
    else:
        if type(a) == int:
            a = a
        elif type(a) == float:
            a = int(a)
    if type(b) != int or type(b) != float:
        raise TypeError('b must be an integer')
    else:
        if type(b) == int:
            b = b
        elif type(b) == float:
            a = int(b)
    return a + b
