#!/usr/bin/env python3

"""
Script to plot a stacked bar graph representing the number of fruit per person.
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Define fruit names and colors
fruits = ['Apples', 'Bananas', 'Oranges', 'Peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Plot the stacked bar graph
bar_width = 0.5
person_labels = ['Farrah', 'Fred', 'Felicia']
x = np.arange(len(person_labels))

fig, ax = plt.subplots()

for i, fruit_type in enumerate(fruits):
    bottom = np.sum(fruit[:i], axis=0)
    ax.bar(x, fruit[i], bar_width, bottom=bottom, label=fruit_type, color=colors[i])

# Add labels, title, legend, and adjust axes
ax.set_xlabel('Person')
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_xticks(x)
ax.set_xticklabels(person_labels)
ax.set_yticks(np.arange(0, 81, 10))
ax.set_ylim(0, 80)
ax.legend()

plt.show()
