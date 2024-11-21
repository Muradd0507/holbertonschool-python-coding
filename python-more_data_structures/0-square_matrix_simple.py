#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in range(len(matrix)):
        k = map(lambda x: x ** 2, matrix[i])
        mat.append(list(k))

    return mat
