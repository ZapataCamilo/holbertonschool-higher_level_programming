#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    N_matrix = []
    for i in matrix:
        N_matrix.append(list(map(lambda x: x**2, i)))
    return N_matrix
