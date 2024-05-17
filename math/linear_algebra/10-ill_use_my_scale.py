#!/usr/bin/env python3


"""
This script defines a function np_shape(matrix) that calculates the shape of a numpy.ndarray
without using loops, conditionals, or imports.
"""


def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray without using loops, conditionals, or imports.

    Parameters:
    matrix (numpy.ndarray): The numpy array.
    """
    return getattr(matrix, 'shape', ()) * hasattr(matrix, 'shape')
