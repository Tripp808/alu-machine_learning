#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the datasets
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Filter timestamps
start_timestamp = 1417411980
end_timestamp = 1417417980
df1_filtered = df1.loc[start_timestamp:end_timestamp]
df2_filtered = df2.loc[start_timestamp:end_timestamp]

# Concatenate the dataframes with keys
df = pd.concat([df2_filtered, df1_filtered], keys=['bitstamp', 'coinbase'])

# Rearrange MultiIndex levels
df = df.swaplevel(0, 1).sort_index(level=0)

# Display the resulting DataFrame
print(df)
