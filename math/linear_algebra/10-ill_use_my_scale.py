#!/usr/bin/env python3


"""
Script for shape
"""


def np_shape(matrix):
    """
    return matrix
    """
    return getattr(matrix, 'shape', ()) * hasattr(matrix, 'shape')
