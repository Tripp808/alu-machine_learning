#!/usr/bin/env python3
"""
Module to calculate the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Parameters:
    poly (list): List of coefficients. The index represents the power of x.

    Returns:
    list: Derivative of the polynomial. Returns [0] if the derivative is zero.
    """
    if not isinstance(poly, list) or \
       not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivative = [i * poly[i] for i in range(1, len(poly))]

    return derivative if derivative else [0]


if __name__ == "__main__":
    poly = [5, 3, 0, 1]
    print(poly_derivative(poly))
