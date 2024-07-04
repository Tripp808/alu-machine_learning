#!/usr/bin/env python3


import numpy as np

def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Parameters:
    images (numpy.ndarray): The images to be convolved with shape (m, h, w)
    kernel (numpy.ndarray): The kernel to be used for the convolution with shape (kh, kw)

    Returns:
    numpy.ndarray: The convolved images with shape (m, h-kh+1, w-kw+1)
    """
    # Extract dimensions from the input images and kernel
    m, h, w = images.shape
    kh, kw = kernel.shape
    
    # Calculate the dimensions of the output
    output_h = h - kh + 1
    output_w = w - kw + 1
    
    # Initialize the output array with zeros
    output = np.zeros((m, output_h, output_w))
    
    # Perform the convolution operation
    for i in range(output_h):
        for j in range(output_w):
            # Extract the current region of interest
            region = images[:, i:i+kh, j:j+kw]
            # Perform element-wise multiplication and sum the results
            output[:, i, j] = np.sum(region * kernel, axis=(1, 2))
    
    return output
