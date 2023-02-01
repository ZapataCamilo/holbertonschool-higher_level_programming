#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        matrix_final = '\n'.join([' '.join(['{:d}\
    '.format(item) for item in row]) for row in matrix])
        print(matrix_final)
