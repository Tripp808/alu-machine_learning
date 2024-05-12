#!/usr/bin/env python3

"""
Script to plot all 5 previous graphs in one figure.
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate data for plots
x0 = np.arange(0, 11)
y0 = x0 ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a figure and subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# Plot 1: x0 vs y0
axs[0, 0].plot(x0, y0)
axs[0, 0].set_xlabel('X')
axs[0, 0].set_ylabel('Y')
axs[0, 0].set_title('Plot 1', fontsize='x-small')

# Plot 2: x1 vs y1
axs[0, 1].scatter(x1, y1, color='magenta')
axs[0, 1].set_xlabel('Height (in)')
axs[0, 1].set_ylabel('Weight (lbs)')
axs[0, 1].set_title("Men's Height vs Weight", fontsize='x-small')

# Plot 3: x2 vs y2
axs[1, 0].plot(x2, y2, color='red')
axs[1, 0].set_xlabel('Time (years)')
axs[1, 0].set_ylabel('Fraction Remaining')
axs[1, 0].set_title('Exponential Decay of C-14', fontsize='x-small')

# Plot 4: x3 vs y31 and y32
axs[1, 1].plot(x3, y31, 'r--', label='C-14')
axs[1, 1].plot(x3, y32, 'g-', label='Ra-226')
axs[1, 1].set_xlabel('Time (years)')
axs[1, 1].set_ylabel('Fraction Remaining')
axs[1, 1].set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
axs[1, 1].legend(loc='upper right')

# Plot 5: Histogram
axs[2, 0].hist(student_grades, bins=np.arange(0, 101, 10), edgecolor='black')
axs[2, 0].set_xlabel('Grades')
axs[2, 0].set_ylabel('Number of Students')
axs[2, 0].set_title('Project A', fontsize='x-small')

# Empty plot to make space for the big plot
axs[2, 1].axis('off')

# Title for the entire figure
fig.suptitle('All in One', fontsize='x-small')

plt.tight_layout()
plt.show()
