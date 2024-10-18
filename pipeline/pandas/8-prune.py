#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove entries where the 'Close' column is NaN
df = df.dropna(subset=['Close'])

# Print the top 5 rows of the cleaned DataFrame
print(df.head())
