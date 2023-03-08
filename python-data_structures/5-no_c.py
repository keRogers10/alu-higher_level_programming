#!/usr/bin/python3
def no_c(my_string):
    new = []
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            pass
        else:
            new.append(new[i])
    return "".join(new)
