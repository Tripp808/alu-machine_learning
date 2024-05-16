#!/usr/bin/env python3


"""Slice a matrix into specified parts."""


import numpy as np

# Define the matrix
matrix = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]])

# Slice the matrix to obtain the middle two rows
mat1 = matrix[1:3]

# Slice the matrix to obtain the middle two columns
mat2 = matrix[:, 2:4]

# Slice the matrix to obtain the bottom-right 3x3 matrix
mat3 = matrix[1:, 3:]

# Display the sliced matrices
print("The middle two rows of the matrix are:\n{}".format(mat1))
print("The middle two columns of the matrix are:\n{}".format(mat2))
print("The bottom-right, square, 3x3 matrix is:\n{}".format(mat3))
