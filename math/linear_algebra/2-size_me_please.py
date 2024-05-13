#!/usr/bin/env python3

"""Module to determine the shape of a matrix."""


def matrix_shape(matrix):
    """Determine the shape of a matrix.

    Args:
        matrix (list): A nested list representing a matrix.

    Returns:
        list: A list containing the dimensions of the matrix.

    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    print(matrix_shape(mat1))
    mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
            [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
    print(matrix_shape(mat2))
