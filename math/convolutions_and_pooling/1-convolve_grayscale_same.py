#!/usr/bin/env python3


"""
Module for performing same convolutions on grayscale images.
"""

import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images.

    Parameters:
    images (numpy.ndarray): The images to be convolved with shape (m, h, w)
    kernel (numpy.ndarray): The kernel with shape (kh, kw)

    Returns:
    numpy.ndarray: The convolved images with shape (m, h, w)
    """
    # Extract dimensions from the input images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the padding for height and width
    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2

    # Pad the images with zeros
    padded_images = np.pad(images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)

    # Initialize the output array with zeros
    output = np.zeros((m, h, w))

    # Perform the convolution operation
    for i in range(h):
        for j in range(w):
            # Extract the current region of interest
            region = padded_images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the results
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))
    
    return output
