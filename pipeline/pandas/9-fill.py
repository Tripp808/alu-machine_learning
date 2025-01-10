#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the data from the CSV file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the Weighted_Price column
df = df.drop(columns=['Weighted_Price'])

# Fill missing values
df['Close'].fillna(method='ffill', inplace=True)  # Fill missing Close values with the previous row value
df[['High', 'Low', 'Open']] = df[['High', 'Low', 'Open']].fillna(df['Close'])  # Fill missing High, Low, Open with Close value
df[['Volume_(BTC)', 'Volume_(Currency)']] = df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0)  # Fill missing Volume with 0

# Print the top and bottom rows of the filled DataFrame
print(df.head())
print(df.tail())
