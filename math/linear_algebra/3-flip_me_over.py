#!/usr/bin/env python3

"""
This module provides functions for matrix operations.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list): The input 2D matrix.

    Returns:
        list: The transpose of the input matrix.
    """
    # Get the dimensions of the input matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize a new matrix with dimensions swapped
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    print(mat1)
    print(matrix_transpose(mat1))
    mat2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25],
        [26, 27, 28, 29, 30],
    ]
    print(mat2)
    print(matrix_transpose(mat2))
