#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    k = 1
    for i in matrix:
        for j in i:
            if k % 3 != 0:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="\n")
            k += 1
