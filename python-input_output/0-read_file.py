#!/usr/bin/python3
""" The module to open file basd on file name"""


def read_file(filename=''):
    """new func to define our functionality"""
    with open("filename", "r", encoding="utf-8") as f:
        new = f.read()
        print(new, end="")
