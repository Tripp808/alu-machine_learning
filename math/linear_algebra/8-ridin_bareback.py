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
        list: multiplication of mat1 and mat2.
    """
    # Check if matrices can be multiplied (columns of mat1 == rows of mat2)
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize result matrix
    result = []

    # Store the number of columns in mat1
    mat1_cols = len(mat1[0])

    # Perform matrix multiplication
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            # Calculate dot product
            dot_product = sum(
                m1 * m2 for m1, m2 in zip(mat1[i], (row[j] for row in mat2))
            )
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
    print(mat_mul(mat1, mat2))
