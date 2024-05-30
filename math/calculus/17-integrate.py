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
    if not isinstance(poly, list) or not poly:
        return None

    if not isinstance(C, (int, float)):
        return None

    integral = [C]

    for i, coeff in enumerate(poly):
        power = i + 1
        if not isinstance(coeff, (int, float)):
            return None
        if coeff == 0:
            integral.append(0)
        else:
            new_coeff = coeff / power
            if isinstance(C, float) and new_coeff.is_integer():
                new_coeff = int(new_coeff)
            integral.append(new_coeff)

    if len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral


if __name__ == "__main__":
    print(poly_integral([0]))  # Output: [0]
    print(poly_integral([5]))  # Output: [0, 5]
   
