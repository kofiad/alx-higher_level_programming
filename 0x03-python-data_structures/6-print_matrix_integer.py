#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for e in range(len(matrix[row])):
            print("{:d}".format(matrix[row][e]), end=" ")
        print()
