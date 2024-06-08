#!/usr/bin/env python3
"""
Normal Distribution Module
"""


class Normal:
    """
    Represents a Normal distribution
    """

    def __init__(self, data=None, mean=0.0, stddev=1.0):
        """
        Initializes the Normal distribution

        Parameters:
        - data (list): Data to estimate the distribution
        - mean (float): Mean of the distribution
        - stddev (float): Standard deviation of the distribution

        Sets mean and stddev as floats. Raises:
        - ValueError if stddev <= 0
        - TypeError if data is not a list
        - ValueError if data has fewer than 2 values
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value

        Parameters:
        - x (float): The x-value

        Returns:
        - The z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score

        Parameters:
        - z (float): The z-score

        Returns:
        - The x-value of z
        """
        return z * self.stddev + self.mean

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value

        Parameters:
        - x (float): The x-value

        Returns:
        - The PDF value for x
        """
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        base = 1 / (self.stddev * (2 * 3.141592653589793) ** 0.5)
        return base * 2.718281828459045 ** exponent

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value

        Parameters:
        - x (float): The x-value

        Returns:
        - The CDF value for x
        """
        z = self.z_score(x)
        erf = (2 / (3.141592653589793 ** 0.5)) * (
            z - (z ** 3) / 3 + (z ** 5) / 10 - (z ** 7) / 42 + (z ** 9) / 216
        )
        return 0.5 * (1 + erf)


if __name__ == "__main__":
    # Simulating data manually without using numpy
    data = [
        83.169, 61.245, 64.433, 75.438, 69.456, 78.019,
        73.750, 60.645, 81.195, 70.297, 68.043, 69.419,
        70.550, 76.255, 58.562, 61.468, 58.479, 57.548,
        75.155, 66.690, 64.111, 75.368, 62.766, 66.163,
        82.022, 68.274, 64.600, 76.830, 65.387, 75.590,
        71.177, 69.915, 74.887, 80.064, 69.556, 71.746,
        68.746, 61.726, 65.569, 77.013, 65.398, 80.182,
        80.230, 72.259, 65.436, 58.418, 76.052, 74.174,
        78.872, 66.065, 70.660, 76.293, 62.406, 68.419,
        59.527, 80.892, 74.077, 58.736, 62.743, 62.099,
        63.731, 71.822, 80.359, 68.994, 64.794, 77.607,
        70.596, 57.929, 68.944, 66.452, 62.423, 58.622,
        70.290, 65.098, 68.399, 72.126, 61.426, 69.230,
        76.526, 67.530, 73.657, 64.174, 64.335, 69.823,
        73.382, 75.638, 79.039, 76.097, 71.533, 79.045,
        79.611, 69.913, 70.388, 78.852, 77.167, 70.872,
        61.234, 66.826, 67.780, 70.660
    ]

    n1 = Normal(data)
    print('PHI(90):', n1.cdf(90))

    n2 = Normal(mean=70, stddev=10)
    print('PHI(90):', n2.cdf(90))
