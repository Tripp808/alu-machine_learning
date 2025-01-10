#!/usr/bin/env python3
"""Module to flip an image horizontally."""

import tensorflow as tf


def flip_image(image):
    """Flips an image horizontally.

    Args:
        image (tf.Tensor): A 3D tensor containing the image to flip.

    Returns:
        tf.Tensor: The horizontally flipped image.
    """
    # Ensure the input is a valid 3D tensor (height, width, channels)
    if len(image.shape) != 3:
        raise ValueError("Input image must be a 3D tensor with shape [height, width, channels]")
    
    return tf.image.flip_left_right(image)
