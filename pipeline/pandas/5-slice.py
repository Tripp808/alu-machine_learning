#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Slice the DataFrame to take every 60th row for specified columns
df = df.loc[:, ['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60]

# Print the last few rows of the sliced DataFrame
print(df.tail())
