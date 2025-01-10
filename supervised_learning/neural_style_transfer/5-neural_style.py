#!/usr/bin/env python3
"""
Defines class NST that performs tasks for neural style transfer
"""

import numpy as np
import tensorflow as tf
from tensorflow.python.keras.applications import vgg19
from tensorflow.python.keras.models import Model
from tensorflow.python.keras import backend as K


class NST:
    """
    Performs tasks for Neural Style Transfer

    public class attributes:
        style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                        'block4_conv1', 'block5_conv1']
        content_layer = 'block5_conv2'

    instance attributes:
        style_image: preprocessed style image
        content_image: preprocessed content image
        alpha: weight for content cost
        beta: weight for style cost
        model: the Keras model used to calculate cost
        gram_style_features: list of gram matrices from style layer outputs
        content_feature: the content layer output of the content image
    """

    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for Neural Style Transfer class

        parameters:
            style_image [numpy.ndarray with shape (h, w, 3)]:
                image used as style reference
            content_image [numpy.ndarray with shape (h, w, 3)]:
                image used as content reference
            alpha [float]: weight for content cost
            beta [float]: weight for style cost
        """
        if not isinstance(style_image, np.ndarray) or len(style_image.shape) != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or len(content_image.shape) != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta
        self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixel values are between 0 and 1
        and its largest side is 512 pixels
        """
        h, w, _ = image.shape
        if h > w:
            h_new = 512
            w_new = int(w * (512 / h))
        else:
            w_new = 512
            h_new = int(h * (512 / w))

        image_resized = tf.image.resize_images(image, (h_new, w_new), method=tf.image.ResizeMethod.BICUBIC)
        image_scaled = image_resized / 255.0
        return np.expand_dims(image_scaled, axis=0)

    def load_model(self):
        """
        Creates the model used to calculate cost from VGG19 Keras base model
        """
        vgg = vgg19.VGG19(include_top=False, weights='imagenet')
        outputs = [vgg.get_layer(name).output for name in self.style_layers + [self.content_layer]]
        self.model = Model(inputs=vgg.input, outputs=outputs)

    @staticmethod
    def gram_matrix(input_layer):
        """
        Calculates gram matrices
        """
        if not isinstance(input_layer, (tf.Tensor, tf.Variable)):
            raise TypeError("input_layer must be a tensor or variable")
        shape = K.shape(input_layer)
        _, h, w, c = shape[0], shape[1], shape[2], shape[3]
        features = K.reshape(input_layer, (h * w, c))
        gram = K.dot(K.transpose(features), features)
        return gram / tf.cast(h * w, tf.float32)

    def generate_features(self):
        """
        Extracts the features used to calculate neural style cost
        """
        style_image_preprocessed = vgg19.preprocess_input(self.style_image * 255)
        content_image_preprocessed = vgg19.preprocess_input(self.content_image * 255)

        style_outputs = self.model.predict(style_image_preprocessed)[:-1]
        content_output = self.model.predict(content_image_preprocessed)[-1]

        self.gram_style_features = [self.gram_matrix(output) for output in style_outputs]
        self.content_feature = content_output

    def layer_style_cost(self, style_output, gram_target):
        """
        Calculates the style cost for a single layer
        """
        gram_style = self.gram_matrix(style_output)
        return K.mean(K.square(gram_style - gram_target))

    def style_cost(self, style_outputs):
        """
        Calculates the style cost for generated image
        """
        style_cost = 0
        weight = 1.0 / len(self.style_layers)
        for i, style_output in enumerate(style_outputs):
            style_cost += weight * self.layer_style_cost(style_output, self.gram_style_features[i])
        return style_cost
