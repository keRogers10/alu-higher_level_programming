#!/usr/bin/python3
"""
program that inherit from  a list
"""

class MyList():
    """initialisation function"""

    def __init__ (self, list=[]):
        self.list = list

    def print_sorted(self):
        return self.list.sort()
