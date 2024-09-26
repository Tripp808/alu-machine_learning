#!/usr/bin/env python3
""" Training with momentum
"""

import tensorflow as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """
    Creates the training operation for a neural network in tensorflow using
    the RMSProp optimization algorithm.

    Parameters:
    - loss: is the loss of the network
    - alpha: is the learning rate
    - beta2: is the RMSProp weight
    - epsilon: is a small number to avoid division by zero

    Returns:
    The RMSProp optimization operation.
    """
    optimizer = tf.train.RMSPropOptimizer(learning_rate=alpha,
                                          decay=beta2,
                                          epsilon=epsilon)
    train_op = optimizer.minimize(loss)
    return train_op
