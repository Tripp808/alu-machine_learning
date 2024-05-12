#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

plt.plot(np.arange(0, 11), y, 'r-')  # 'r-' for solid red line
plt.xlim(0, 10)  # setting x-axis limit
plt.xlabel('X-axis')  # label for x-axis
plt.ylabel('Y-axis')  # label for y-axis
plt.title('Line Plot of y = x^3')  # title of the plot
plt.grid(True)  # enabling grid
plt.show()  # displaying the plot
