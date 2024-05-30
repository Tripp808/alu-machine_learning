#!/usr/bin/env python3
"""
Module to calculate the derivative of a polynomial.
"""


def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.
    
    :param poly: List of coefficients representing the polynomial.
    :type poly: list
    :return: List of coefficients representing the derivative of the polynomial,
             or None if poly is not valid.
    """
    if not isinstance(poly, list) or not all(isinstance(coef, (int, float)) for coef in poly):
        return None
    
    # If the polynomial is a constant (length of list is 1), derivative is 0
    if len(poly) == 1:
        return [0]
    
    # Calculate the derivative
    derivative = [coef * i for i, coef in enumerate(poly)][1:]
    
    return derivative

if __name__ == "__main__":
    poly = [5, 3, 0, 1]
    print(poly_derivative(poly))  # Output should be [3, 0, 3]
