#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        pass
    else:
        for i in matrix:
            for j in i:
                print("{:d} ".format(j), end="")
            print()
