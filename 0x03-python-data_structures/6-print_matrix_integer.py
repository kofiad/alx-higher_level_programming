#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for e in row:
            print("{:d}".format(e), end=" ")
        print()
