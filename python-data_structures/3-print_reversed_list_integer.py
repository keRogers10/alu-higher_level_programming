#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = my_list.reverse()
    for n in range(len(new)):
        print('{:d}'.format(new[n]))
