#!/usr/bin/env python3

"""
This module defines a function for concatenating two arrays.
"""


def cat_arrays(arr1, arr2):
    """
    Concatenate two arrays.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list:list containing elements from arr1 followed by elements from arr2.
    """
    return arr1 + arr2


if __name__ == "__main__":
    # Test cases
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [6, 7, 8]
    print(cat_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
    print(arr1)  # Output: [1, 2, 3, 4, 5]
    print(arr2)  # Output: [6, 7, 8]
