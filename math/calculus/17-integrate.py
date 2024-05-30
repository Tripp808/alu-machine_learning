#!/usr/bin/env python3
"""
Module to calculate the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Parameters:
    poly (list): List of coefficients representing a polynomial.
    C (int): Integration constant. Default is 0.

    Returns:
    list: Coefficients of the integral of the polynomial.
    """
    if not isinstance(poly, list) or \
       not all(isinstance(x, (int, float)) for x in poly):
        return None

    if not isinstance(C, int):
        return None

    integral = [C]

    for i, coeff in enumerate(poly):
        power = i + 1
        if isinstance(coeff, int):
            integral.append(coeff // power)
        else:
            integral.append(coeff / power)

    return integral


if __name__ == "__main__":
    poly = [5, 3, 0, 1]
    print(poly_integral(poly))
