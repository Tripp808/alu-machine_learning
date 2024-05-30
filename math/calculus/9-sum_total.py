#!/usr/bin/env python3


"""
Module to calculate the summation of squares of the first n natural numbers.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares of the first n natural numbers.
    
    :param n: The number up to which squares are summed.
    :type n: int
    :return: The sum of squares of the first n natural numbers, or None if n is not valid.
    :rtype: int or None
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
