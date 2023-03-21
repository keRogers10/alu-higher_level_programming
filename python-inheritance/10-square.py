#!/usr/bin/python3
"""same as triangle this is a module to overright charachters
of rectangler
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ a class that inherit rectangle as a parent class"""

    def __init__(self, size):
        size.integer_validator('size', size)
        self.__size = size

    def area(self):
        
        return self.__size**2
