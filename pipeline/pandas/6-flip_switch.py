#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Transpose the DataFrame and sort by index in reverse order
df = df.T.sort_index(ascending=False)

# Print the last 8 rows of the transposed and sorted DataFrame
print(df.tail(8))
