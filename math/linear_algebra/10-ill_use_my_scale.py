#!/usr/bin/env python3

"""
Module to calculate the shape of a NumPy array.
"""

import numpy as np

def np_shape(matrix):
    """
    Calculates the shape of a NumPy array.

    Args:
    - matrix (numpy.ndarray): Input NumPy array.

    Returns:
    - tuple of ints: The shape of the input array.
    """
    return matrix.shape

if __name__ == "__main__":
    mat1 = np.array([1, 2, 3, 4, 5, 6])
    mat2 = np.array([])
    mat3 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                     [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
    
    print(np_shape(mat1))
    print(np_shape(mat2))
    print(np_shape(mat3))
