import pandas as pd

def from_file(filename, delimiter):
    # Use pandas read_csv to load the file into a DataFrame, specifying the delimiter
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
