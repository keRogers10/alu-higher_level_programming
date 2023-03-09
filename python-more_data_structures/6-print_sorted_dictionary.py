#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = list(a_dictionary.keys())
    now = new.sort()
    for i in now:
        print("{}: {}".format(i, a_dictionary.get(i)))
