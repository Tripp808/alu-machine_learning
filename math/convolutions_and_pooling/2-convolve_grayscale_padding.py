#!/usr/bin/env python3


"""
Module for performing convolutions on grayscale images with custom padding.
"""


import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    """
    Performs a convolution on grayscale images with custom padding.

    Parameters:
    images (numpy.ndarray): The images to be convolved with shape (m, h, w)
    kernel (numpy.ndarray): The kernel with shape (kh, kw)
    padding (tuple): The padding for the height and width of the image (ph, pw)

    Returns:
    numpy.ndarray: The convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape
    ph, pw = padding

    # Pad the images with zeros
    padded_images = np.pad(
        images,
        ((0, 0), (ph, ph), (pw, pw)),
        mode='constant',
        constant_values=0
    )

    # Calculate the dimensions of the output
    output_h = h + 2 * ph - kh + 1
    output_w = w + 2 * pw - kw + 1

    # Initialize the output array with zeros
    output = np.zeros((m, output_h, output_w))

    # Perform the convolution operation
    for i in range(output_h):
        for j in range(output_w):
            # Extract the current region of interest
            region = padded_images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the results
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))

    return output
