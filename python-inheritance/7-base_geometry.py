#!/usr/bin/python3
"""
this is an empty class
"""


class BaseGeometry():
    """
    here we will define some functions inside a class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} must be an integer")
        if value < 0:
            raise ValueError(f"{value} must be greater than 0")
