#!/usr/bin/env python3


"""
element wise add, sub, product...
"""


def np_elementwise(mat1, mat2):
    """
    Returns:
    tuple: Element-wise sum, difference, product, and quotient, respectively.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
