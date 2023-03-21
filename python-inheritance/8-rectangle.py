#!/usr/bin/python3
"""
a class that will inherit characters from base geometry
again we will assign to instances of
height and width
"""


class Rectangle(BaseGeometry):
    """
    we have to define some of properties
    of rectangle based on base geometry

    args:
    width 
    height
    """

    def __init__(self, width, height):
        if type(width) != int or type(height) != int:
            raise TypeError("Wrong type")
        if width < 0 or height < 0:
            raise ValueError("both width and height must be positive integers)
        else:
        self.__width = width
        self.__height = height
