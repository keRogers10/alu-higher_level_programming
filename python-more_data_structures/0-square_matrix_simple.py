#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for i in new_matrix:
        for o in i:
            o = o**2
    return new_matrix
