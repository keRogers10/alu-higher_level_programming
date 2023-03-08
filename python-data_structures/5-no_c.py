#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in range(len(my_string)):
        if my_string[i] != 'C' or my_string[i] != 'c':
            new.append(my_string[i])
        else:
            pass
    return "".join(new)
