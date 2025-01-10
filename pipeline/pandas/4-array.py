#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Select the last 10 rows of the 'High' and 'Close' columns
A = df[['High', 'Close']].tail(10).to_numpy()

# Print the numpy array
print(A)
