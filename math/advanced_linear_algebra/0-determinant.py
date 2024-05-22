#!/usr/bin/env python3


"""
This module provides a function to calculate the determinant of a matrix.
"""


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The matrix whose determinant is to be calculated.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is square
    num_rows = len(matrix)
    if num_rows == 0 or any(len(row) != num_rows for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case for 0x0 matrix
    if num_rows == 0:
        return 1

    # Base case for 1x1 matrix
    if num_rows == 1:
        return matrix[0][0]

    # Recursive calculation for larger matrices
    det = 0
    for j in range(num_rows):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += (-1) ** j * matrix[0][j] * determinant(minor)
    return det
