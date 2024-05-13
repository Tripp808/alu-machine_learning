#!/usr/bin/env python3

def matrix_transpose(matrix):
    # Get the dimensions of the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transpose_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate over the original matrix and fill the transpose matrix
    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix

# Test cases
mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))

mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))
