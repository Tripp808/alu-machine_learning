#!/usr/bin/env python3
"""
Exponential Distribution Module
"""


class Exponential:
    """
    Represents an Exponential distribution
    """

    def __init__(self, data=None, lambtha=1.0):
        """
        Initializes the Exponential distribution

        Parameters:
        - data (list): Data to estimate the distribution
        - lambtha (float): Expected number of occurrences in a given timeframe

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
            self.lambtha = 1 / (sum(data) / len(data))


if __name__ == "__main__":
    # Simulating data manually without using numpy
    data = [0.5, 0.7, 0.2, 0.4, 0.6, 0.8, 0.3, 0.5, 0.7, 0.9, 
            0.2, 0.4, 0.6, 0.8, 0.1, 0.3, 0.5, 0.7, 0.9, 0.2,
            0.4, 0.6, 0.8, 0.3, 0.5, 0.7, 0.9, 0.4, 0.6, 0.8,
            0.2, 0.4, 0.6, 0.8, 0.3, 0.5, 0.7, 0.9, 0.1, 0.3,
            0.5, 0.7, 0.9, 0.2, 0.4, 0.6, 0.8, 0.3, 0.5, 0.7,
            0.9, 0.4, 0.6, 0.8, 0.2, 0.4, 0.6, 0.8, 0.3, 0.5,
            0.7, 0.9, 0.1, 0.3, 0.5, 0.7, 0.9, 0.2, 0.4, 0.6,
            0.8, 0.3, 0.5, 0.7, 0.9, 0.4, 0.6, 0.8, 0.2, 0.4,
            0.6, 0.8, 0.3, 0.5, 0.7, 0.9, 0.1, 0.3, 0.5, 0.7,
            0.9, 0.2, 0.4, 0.6, 0.8, 0.3, 0.5, 0.7, 0.9, 0.4]

    e1 = Exponential(data)
    print('Lambtha:', e1.lambtha)

    e2 = Exponential(lambtha=2)
    print('Lambtha:', e2.lambtha)
