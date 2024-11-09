#!/usr/bin/env python3
"""Module to change the hue of an image."""

import tensorflow as tf

def change_hue(image, delta):
    """Changes the hue of an image.

    Args:
        image (tf.Tensor): A 3D tensor containing the image to change.
        delta (float): The amount by which to adjust the hue. Should be between -1 and 1.

    Returns:
        tf.Tensor: The hue-adjusted image.
    """
    # Adjust the hue of the image
    altered_image = tf.image.adjust_hue(image, delta)

    return altered_image
