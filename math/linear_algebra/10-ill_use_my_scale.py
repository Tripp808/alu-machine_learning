#!/usr/bin/env python3


"""
This script defines a function np_shape(matrix).
"""


def np_shape(matrix):
    """
    Calculates the shape of a numpy.ndarray without using loops, conditionals, or imports.
    """
    return getattr(matrix, 'shape', ()) * hasattr(matrix, 'shape')
