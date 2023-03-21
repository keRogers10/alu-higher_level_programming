#!/usr/bin/python3
"""same as triangle this is a module to overright charachters
of rectangler
"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ a class that inherit rectangle as a parent class"""

    def __init__(self, size):
        size.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):

        return super().area()
