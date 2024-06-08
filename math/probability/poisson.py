#!/usr/bin/env python3
"""
Poisson Distribution Module
"""


class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.0):
        """
        Initializes the Poisson distribution

        Parameters:
        - data (list): Data to estimate the distribution
        - lambtha (float): Expected occurrences in a given timeframe

        Sets lambtha as a float. Raises:
        - ValueError if lambtha <= 0
        - TypeError if data is not a list
        - ValueError if data has fewer than 2 values
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))


if __name__ == "__main__":
    # Simulating data manually without using numpy
    data = [5, 4, 6, 6, 3, 7, 5, 6, 4, 5, 5, 6, 4, 4, 5, 5, 5, 5, 4, 6,
            6, 6, 5, 4, 7, 5, 6, 5, 5, 6, 5, 4, 6, 5, 5, 6, 5, 5, 4, 5,
            6, 4, 5, 5, 4, 5, 5, 6, 5, 5, 4, 5, 6, 5, 6, 6, 5, 6, 4, 5,
            6, 4, 5, 6, 4, 4, 5, 5, 5, 4, 4, 6, 5, 5, 5, 5, 5, 6, 4, 5,
            4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 6]

    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
