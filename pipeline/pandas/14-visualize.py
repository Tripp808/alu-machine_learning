#!/usr/bin/env python3

from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the dataset
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the Weighted_Price column
df.drop(columns=['Weighted_Price'], inplace=True)

# Rename the Timestamp column to Date
df.rename(columns={'Timestamp': 'Date'}, inplace=True)

# Convert timestamp values to datetime
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Set the Date column as the index
df.set_index('Date', inplace=True)

# Fill missing values
df['Close'].fillna(method='ffill', inplace=True)  # Forward fill for Close
df[['High', 'Low', 'Open']].fillna(df['Close'], inplace=True)  # Fill with Close for High, Low, Open
df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0, inplace=True)  # Set to 0 for Volume columns

# Filter data for 2017 and beyond
df_filtered = df['2017':]

# Resample the data to daily intervals and aggregate
daily_data = df_filtered.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plot the daily aggregated data
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['Close'], label='Close', color='blue', linewidth=1.5)
plt.title('Daily Average Close Price (2017 and beyond)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
