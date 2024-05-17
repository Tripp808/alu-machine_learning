#!/usr/bin/env python3

def np_transpose(matrix):
    """
    Transpose the given matrix.

    Args:
    matrix: A matrix that can be interpreted as a numpy ndarray.
            It can be a 1D, 2D, or 3D matrix.

    Returns:
    Transposed version of the input matrix.
    """
    return matrix.T

# Example usage (this will run directly when the script is executed):

# Transpose a 1D array
array_1d = [[1, 2, 3, 4, 5, 6]]
print("Transpose of 1D array:")
print(np_transpose(array_1d))
print()

# Transpose an empty 2D array
array_2d_empty = [[], []]
print("Transpose of empty 2D array:")
print(np_transpose(array_2d_empty))
print()

# Transpose a 3D array
array_3d = [[[ 1, 11],
             [ 6, 16]],
             
            [[ 2, 12],
             [ 7, 17]],
             
            [[ 3, 13],
             [ 8, 18]],
             
            [[ 4, 14],
             [ 9, 19]],
             
            [[ 5, 15],
             [10, 20]]]
print("Transpose of 3D array:")
print(np_transpose(array_3d))
print()

# Transpose another 3D array
array_3d_another = [[[ 1,  2,  3,  4,  5],
                     [ 6,  7,  8,  9, 10]],

                    [[11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20]]]
print("Transpose of another 3D array:")
print(np_transpose(array_3d_another))
