#!/usr/bin/python3
"""This function is to testing"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix"""

    ms1 = 'matrix must be a matrix (list of lists) of integers/floats'
    new_mtx = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for ind_list in matrix:
        if len(ind_list) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        sub_list = []
        for ind_num in ind_list:
            if not isinstance(ind_num, (int, float)):
                raise TypeError(ms1)
            else:
                sub_list.append(round(ind_num / div, 2))
        new_mtx.append(sub_list)

    return new_mtx
