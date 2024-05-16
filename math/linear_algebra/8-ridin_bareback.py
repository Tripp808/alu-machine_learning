#!/usr/bin/env python3

"""
This module defines a function for performing matrix multiplication.
"""


def mat_mul(mat1, mat2):
    """
    Perform matrix multiplication.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.

    Returns:
        list: matrix resulting from multiplication of mat1 and mat2.
    """
    # Check if matrices can be multiplied (columns of mat1 == rows of mat2)
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix
    result = []

    # Perform matrix multiplication
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            # Dot product of row i of mat1 and column j of mat2
            dot_product = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))
            row.append(dot_product)
        result.append(row)

    return result


if __name__ == "__main__":
    # Test case
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
    print(mat_mul(mat1, mat2))  # Output: [[11, 14, 17, 20], [23, 30, 37, 44], [35, 46, 57, 68]]
