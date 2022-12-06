#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (len(matrix) == 1 and len(matrix[0]) == 0) or len(matrix) == 0:
        print("")
        return
    for i in matrix:
        for j in range(len(i)):
            if j == len(i) - 1:
                print("{:d}\n".format(i[j]), end="")
            else:
                print("{:d} ".format(i[j]), end="")
