#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in range(len(my_string)):
        if my_string[i] != 'S' or my_string[i] != 's':
            new.append(my_string[i])
    return "".join(new)
