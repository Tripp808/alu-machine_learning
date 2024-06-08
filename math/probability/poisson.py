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
    import numpy as np

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
