#!/usr/bin/env python3
'''
Module for calculating the integral of a polynomial.
'''


def poly_integral(poly, C=0):
    '''
    Calculate the integral of a polynomial.

    Parameters:
    poly (list): Coefficients list where index represents power of x.
    C (int/float): Integration constant. Defaults to 0.

    Returns:
    list: Coefficients list representing the polynomial's integral,
          or None if input is invalid.
    '''
    # Validate input
    if not isinstance(poly, list) or not poly:
        return None
    if not isinstance(C, (int, float)):
        return None
    for coefficient in poly:
        if not isinstance(coefficient, (int, float)):
            return None

    # Convert C to int if it's a float and equal to an integer
    if isinstance(C, float) and C.is_integer():
        C = int(C)

    # Calculate integral
    integral = [C] if C != 0 else [0]
    for power, coefficient in enumerate(poly):
        if coefficient == 0:
            integral.append(0)
        else:
            new_coefficient = coefficient / (power + 1)
            integral.append(int(new_coefficient)
                            if new_coefficient.is_integer()
                            else new_coefficient)

    # Remove last element if 0 and list has more than one element
    if len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral


if __name__ == "__main__":
    print(poly_integral([0]))  # Output: [0]
    print(poly_integral([5]))  # Output: [0, 5]
