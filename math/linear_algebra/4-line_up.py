#!/usr/bin/env python3

"""
Module to add two arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): First array.
        arr2 (list): Second array.

    Returns:
        list: list containing the element-wise sum of arr1 and arr2.
    """
    if len(arr1) != len(arr2):
        return None
    else:
        return [
            a + b
            for a, b in zip(arr1, arr2)
        ]


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))
