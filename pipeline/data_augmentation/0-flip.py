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
    return tf.image.flip_left_right(image)
