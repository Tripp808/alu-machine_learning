#!/usr/bin/env python3


def determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    """
    
    def get_minor(matrix, i, j):
        """Return minor matrix after removing i-th row and j-th column."""
        return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    # Check if matrix is square
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a square matrix")
    
    # Base cases
    if matrix == [[]]:  # 0x0 matrix
        return 1
    if n == 1:  # 1x1 matrix
        return matrix[0][0]
    if n == 2:  # 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    # Recursive case for nxn matrix
    det = 0
    for j in range(n):
        minor = get_minor(matrix, 0, j)
        cofactor = ((-1) ** j) * matrix[0][j]
        det += cofactor * determinant(minor)
    
    return det


if __name__ == '__main__':
    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))  # Expected output: 1
    print(determinant(mat1))  # Expected output: 5
    print(determinant(mat2))  # Expected output: -2
    print(determinant(mat3))  # Expected output: 0
    print(determinant(mat4))  # Expected output: 192
    try:
        print(determinant(mat5))  # Should raise ValueError
    except Exception as e:
        print(e)
    try:
        print(determinant(mat6))  # Should raise ValueError
    except Exception as e:
        print(e)
