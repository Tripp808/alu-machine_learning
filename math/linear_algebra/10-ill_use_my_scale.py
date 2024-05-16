#!/usr/bin/env python3


"""
This script defines a function np_shape(matrix) that calculates the shape of a numpy.ndarray.
"""


def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray.

    Parameters:
    matrix (list): The input list representing a numpy array.

    Returns:
    tuple: A tuple representing the shape of the input array.
    """
    shapes = {
        0: lambda m: (),
        1: lambda m: (len(m),),
        2: lambda m: (len(m), len(m[0])),
        # Extend this pattern to handle higher dimensions needed
    }
    return shapes.get(len(matrix), lambda m: ()) (matrix)

# Sample matrices
mat1 = [1, 2, 3, 4, 5, 6]
mat2 = []
mat3 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
        [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]

# Testing the function
print(np_shape(mat1))
print(np_shape(mat2))
print(np_shape(mat3))
