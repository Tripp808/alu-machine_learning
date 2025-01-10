import pandas as pd

# Define the dictionary with the required columns
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
}

# Create the DataFrame and specify the row labels
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

# df is now the DataFrame with the specified structure
