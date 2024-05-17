#!/usr/bin/env python3

def np_transpose(matrix):
    """
    Transposes the given matrix.

    Parameters:
    matrix: The matrix to be transposed.

    Returns:
    The transposed matrix.
    """
    return [list(row) for row in zip(*matrix)] or [[]]

# Test cases to demonstrate the function
mat1 = [[1, 2, 3, 4, 5, 6]]
mat2 = []
mat3 = [
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
    [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
]

print(np_transpose(mat1))
print(mat1)
print(np_transpose(mat2))
print(mat2)
print(np_transpose(mat3))
print(mat3)
