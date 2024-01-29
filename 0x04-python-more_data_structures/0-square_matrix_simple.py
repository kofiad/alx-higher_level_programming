#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    def square_value(x):
        return x ** 2
    result_matrix = list(map(lambda row: list(map(square_value, row)), matrix))
    return result_matrix
