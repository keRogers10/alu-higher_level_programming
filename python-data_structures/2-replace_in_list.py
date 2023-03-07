#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    length = len(my_list) - 1
    element = my_list[idx]
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        return element
