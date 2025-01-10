#!/usr/bin/env python3
"""
Defines class NST that performs tasks for neural style transfer
"""

import numpy as np
import tensorflow as tf


class NST:
    """
    Performs tasks for Neural Style Transfer
    """

    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for Neural Style Transfer class
        """
        if not isinstance(style_image, np.ndarray) or \
           len(style_image.shape) != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or \
           len(content_image.shape) != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")

        style_h, style_w, style_c = style_image.shape
        content_h, content_w, content_c = content_image.shape
        if style_h <= 0 or style_w <= 0 or style_c != 3:
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)")
        if content_h <= 0 or content_w <= 0 or content_c != 3:
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)")

        if not isinstance(alpha, (float, int)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (float, int)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        tf.enable_eager_execution()

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = float(alpha)
        self.beta = float(beta)
        self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixels values are between 0 and 1
        """
        if not isinstance(image, np.ndarray) or len(image.shape) != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")
        h, w, c = image.shape
        if h <= 0 or w <= 0 or c != 3:
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)")

        if h > w:
            new_h = 512
            new_w = int(w * 512 / h)
        else:
            new_w = 512
            new_h = int(h * 512 / w)

        resized = tf.image.resize(
            np.expand_dims(image, axis=0),
            [new_h, new_w],
            method=tf.image.ResizeMethod.BICUBIC
        )
        rescaled = resized / 255.0
        return tf.clip_by_value(rescaled, 0.0, 1.0)

    def load_model(self):
        """
        Creates the model used to calculate cost from VGG19 Keras base model
        """
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False

        style_outputs = [vgg.get_layer(name).output for name in self.style_layers]
        content_output = vgg.get_layer(self.content_layer).output

        model_outputs = style_outputs + [content_output]
        self.model = tf.keras.models.Model(vgg.input, model_outputs)

    @staticmethod
    def gram_matrix(input_layer):
        """
        Calculates gram matrices
        """
        if not isinstance(input_layer, (tf.Tensor, tf.Variable)):
            raise TypeError("input_layer must be a tensor")
        if len(input_layer.shape) != 4:
            raise TypeError("input_layer must be a tensor of rank 4")

        _, h, w, c = input_layer.shape
        features = tf.reshape(input_layer, [-1, c])
        gram = tf.matmul(features, features, transpose_a=True)
        gram = tf.expand_dims(gram / tf.cast(h * w, tf.float32), 0)
        return gram

    def generate_features(self):
        """
        Extracts the features used to calculate neural style cost
        """
        preprocess_input = tf.keras.applications.vgg19.preprocess_input

        preprocessed_style = preprocess_input(self.style_image * 255.0)
        preprocessed_content = preprocess_input(self.content_image * 255.0)

        outputs_style = self.model(preprocessed_style)
        outputs_content = self.model(preprocessed_content)

        self.gram_style_features = [
            self.gram_matrix(style_output) for style_output in outputs_style[:-1]
        ]
        self.content_feature = outputs_content[-1]

    def layer_style_cost(self, style_output, gram_target):
        """
        Calculates the style cost for a single layer
        """
        gram_style = self.gram_matrix(style_output)
        return tf.reduce_mean(tf.square(gram_style - gram_target))

    def style_cost(self, style_outputs):
        """
        Calculates the style cost for generated image
        """
        if not isinstance(style_outputs, list) or \
           len(style_outputs) != len(self.style_layers):
            raise ValueError(
                "style_outputs must be a list with a length of %d" %
                len(self.style_layers))

        weight = 1.0 / len(self.style_layers)
        total_style_cost = 0
        for i in range(len(self.style_layers)):
            total_style_cost += weight * self.layer_style_cost(
                style_outputs[i], self.gram_style_features[i])
        return total_style_cost
