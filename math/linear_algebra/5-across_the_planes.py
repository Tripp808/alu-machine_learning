#!/usr/bin/env python3

"""
This module defines a function for adding two 2D matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Add two matrices element-wise.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.

    Returns:
        list: matrix resulting from the addition of mat1 and mat2 element-wise.
    """
    # Check if matrices have the same shape
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    # Initialize result matrix
    result = []

    # Iterate over rows
    for i in range(len(mat1)):
        row = []
        # Iterate over columns
        for j in range(len(mat1[0])):
            # Add corresponding elements
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)

    return result


if __name__ == "__main__":
    # Test cases
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))  # Output: [[6, 8], [10, 12]]
    print(mat1)  # Output: [[1, 2], [3, 4]]
    print(mat2)  # Output: [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))  # Output: None
