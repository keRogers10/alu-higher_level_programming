#!/usr/bin/python3
""" The module to open file basd on file name"""

def read_file(filename=''):
    """new func to define our functionality"""
    f = open("filename", "r", encoding="utf-8")
    print(f.read())
    f.close()
