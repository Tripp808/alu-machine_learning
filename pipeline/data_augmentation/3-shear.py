#!/usr/bin/env python3
"""Module to shear an image randomly."""

import tensorflow as tf

def shear_image(image, intensity):
    """Shears an image randomly.

    Args:
        image (tf.Tensor): A 3D tensor containing the image to shear.
        intensity (float): The intensity of the shear.

    Returns:
        tf.Tensor: The sheared image.
    """
    # Generate a random shear angle between -intensity and +intensity
    shear_factor = tf.random.uniform([], minval=-intensity, maxval=intensity, dtype=tf.float32)

    # Create the shear matrix
    shear_matrix = tf.convert_to_tensor([[1.0, shear_factor, 0.0], 
                                         [0.0, 1.0, 0.0]], dtype=tf.float32)
    
    # Apply the shear transformation
    sheared_image = tf.image.transform(image, shear_matrix)

    return sheared_image
