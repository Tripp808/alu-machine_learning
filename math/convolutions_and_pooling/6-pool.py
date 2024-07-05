#!/usr/bin/env python3
"""


import numpy as np
"""

def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images.

    Parameters:
    images (numpy.ndarray): The images to be pooled with shape (m, h, w, c)
    kernel_shape (tuple): The kernel shape for pooling (kh, kw)
    stride (tuple): The stride for the height and width of the image (sh, sw)
    mode (str): The type of pooling ('max' or 'avg')

    Returns:
    numpy.ndarray: The pooled images
    """
    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    output_h = (h - kh) // sh + 1
    output_w = (w - kw) // sw + 1

    pooled_images = np.zeros((m, output_h, output_w, c))

    for i in range(output_h):
        for j in range(output_w):
            region = images[:, i * sh:i * sh + kh, j * sw:j * sw + kw, :]
            if mode == 'max':
                pooled_images[:, i, j, :] = np.max(region, axis=(1, 2))
            elif mode == 'avg':
                pooled_images[:, i, j, :] = np.mean(region, axis=(1, 2))

    return pooled_images
