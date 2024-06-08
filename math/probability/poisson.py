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

    def pmf(self, k):
        """
        Calculates the PMF for a given number of successes

        Parameters:
        - k (int): Number of successes

        Returns:
        - PMF value for k
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285  # Approximation of Euler's number
        lambtha_k = self.lambtha ** k
        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i

        pmf_value = (e ** -self.lambtha) * lambtha_k / k_factorial
        return pmf_value

    def cdf(self, k):
        """
        Calculates the CDF for a given number of successes

        Parameters:
        - k (int): Number of successes

        Returns:
        - CDF value for k
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285  # Approximation of Euler's number
        cdf_value = 0
        for i in range(k + 1):
            lambtha_i = self.lambtha ** i
            i_factorial = 1
            for j in range(1, i + 1):
                i_factorial *= j
            cdf_value += (e ** -self.lambtha) * lambtha_i / i_factorial

        return cdf_value


if __name__ == "__main__":
    # Simulating data manually without using numpy
    data = [5, 4, 6, 6, 3, 7, 5, 6, 4, 5, 5, 6, 4, 4, 5, 5, 5, 5, 4, 6,
            6, 6, 5, 4, 7, 5, 6, 5, 5, 6, 5, 4, 6, 5, 5, 6, 5, 5, 4, 5,
            6, 4, 5, 5, 4, 5, 5, 6, 5, 5, 4, 5, 6, 5, 6, 6, 5, 6, 4, 5,
            6, 4, 5, 6, 4, 4, 5, 5, 5, 4, 4, 6, 5, 5, 5, 5, 5, 6, 4, 5,
            4, 5, 5, 4, 5, 5, 5, 5, 4, 5, 6, 5, 5, 6, 5, 5, 6, 5, 5, 6]

    p1 = Poisson(data)
    print('F(9):', p1.cdf(9))

    p2 = Poisson(lambtha=5)
    print('F(9):', p2.cdf(9))
