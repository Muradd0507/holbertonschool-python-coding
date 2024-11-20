#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    k = 1
    m = 1
    for i in matrix:
        for j in i:
            if k != m:
                m = k
                print("{:d}".format(j), end="\n")
            else:
                print("{:d}".format(j), end=" ")
        k += 1
