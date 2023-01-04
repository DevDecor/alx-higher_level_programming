#!/usr/bin/python3
def matrix_divided(matrix, div):

    empty = []
    buff = []
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if ((not matrix) or (len(matrix) == 0) or not all(
            [isinstance(x, list) for x in matrix]) or not all(
            [all([isinstance(x, int) or isinstance(x, float) for x in par])
                for par in matrix])):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    length = len(matrix[0])
    if (not all([True if len(x) == length else False for x in matrix])):
        raise TypeError('Each row of the matrix must have the same size')
    for i in matrix:
        for j in i:
            buff.append(round(j/div, 2))
        empty.append(buff)
        buff = []
    return empty


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix = None
# if __name__ == "__main__":
#     print(matrix_divided(matrix, 2))
