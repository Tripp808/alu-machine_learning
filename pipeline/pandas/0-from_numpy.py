import pandas as pd
import string

def from_numpy(array):
    # Generate the column labels ('A', 'B', 'C', ..., 'Z') based on the number of columns in the array
    columns = list(string.ascii_uppercase[:array.shape[1]])
    # Create a DataFrame from the numpy array with the generated column labels
    df = pd.DataFrame(array, columns=columns)
    return df
