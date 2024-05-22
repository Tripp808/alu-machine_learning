#!/usr/bin/env python3
"""
Defines function that calculates the definiteness of a matrix
"""


import numpy as np


def definiteness(matrix):
    """
    Calculates the definiteness of a matrix

    parameters:
        matrix [numpy.ndarray of shape(n, n)]:
            matrix whose definiteness should be calculated

    returns:
        one of the following strings indicating definiteness or None:
            "Positive definite"
            "Positive semi-definite"
            "Negative definite"
            "Negative semi-definite"
            "Indefinite"
    """
    if type(matrix) is not np.ndarray:
        raise TypeError("matrix must be a numpy.ndarray")
    if len(matrix.shape) != 2 or matrix.shape[0] != matrix.shape[1] or \
       np.array_equal(matrix, matrix.T) is False:
        return None
    pos_count = 0
    neg_count = 0
    zero_count = 0
    eigenvalues = np.linalg.eig(matrix)[0]
    for value in eigenvalues:
        if value > 0:
            pos_count += 1
        if value < 0:
            neg_count += 1
        if value == 0 or value == 0.:
            zero_count += 1
    if pos_count and zero_count and neg_count == 0:
        return ("Positive semi-definite")
    elif neg_count and zero_count and pos_count == 0:
        return ("Negative semi-definite")
    elif pos_count and neg_count == 0:
        return ("Positive definite")
    elif neg_count and pos_count == 0:
        return ("Negative definite")
    return ("Indefinite")
