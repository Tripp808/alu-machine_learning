#!/usr/bin/env python3

"""
Function for concatenating two matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two matrices along a specific axis.

    Args:
        mat1 (list): The first matrix.
        mat2 (list): The second matrix.
        axis (int, optional): Axis concatenate. Defaults to 0.

    Returns:
        list: new matrix resulting from the concatenation of mat1 and mat2.
    """
    # Check if the matrices can be concatenated along the specified axis
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None


if __name__ == "__main__":
    # Test cases
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6]]
    mat3 = [[7], [8]]
    mat4 = cat_matrices2D(mat1, mat2)
    mat5 = cat_matrices2D(mat1, mat3, axis=1)
    print(mat4)  # Output: [[1, 2], [3, 4], [5, 6]]
    print(mat5)  # Output: [[1, 2, 7], [3, 4, 8]]
    mat1[0] = [9, 10]
    mat1[1].append(5)
    print(mat1)  # Output: [[9, 10], [3, 4, 5]]
    print(mat4)  # Output: [[1, 2], [3, 4], [5, 6]]
    print(mat5)  # Output: [[1, 2, 7], [3, 4, 8]]
