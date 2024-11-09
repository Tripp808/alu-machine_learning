#!/usr/bin/env python3
"""Module to change the brightness of an image randomly."""

import tensorflow as tf

def change_brightness(image, max_delta):
    """Randomly changes the brightness of an image.

    Args:
        image (tf.Tensor): A 3D tensor containing the image to change.
        max_delta (float): The maximum amount by which to change the brightness (both positive and negative).

    Returns:
        tf.Tensor: The brightness-adjusted image.
    """
    # Randomly adjust the brightness of the image within the specified range
    altered_image = tf.image.random_brightness(image, max_delta=max_delta)

    return altered_image
