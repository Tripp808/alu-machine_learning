#!/usr/bin/env python3

"""
Module to plot a line graph.
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_line_graph():
    """
    Function to plot a line graph.
    
    y should be plotted as a solid red line
    The x-axis should range from 0 to 10
    """
    y = np.arange(0, 11) ** 3
    x = np.arange(0, 11)

    plt.plot(x, y, color='red')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Graph')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_line_graph()
