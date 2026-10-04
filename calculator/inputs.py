"""Read a CSV input source; choosing and performing math belong elsewhere."""
from pathlib import Path
import pandas as pd

'''new version of reading CSV input source to fit with its tests'''
'''made as part of part five'''
'''tests can be found in test_inputs.py'''

def read_csv_values(path, column="value"):
    frame = pd.read_csv(Path(path))
    if column not in frame.columns:
        raise ValueError(f"CSV must contain a column named {column}.")
    return frame[column].tolist()

'''
def read_csv_values(path, column="value"):
    # edited the header to fulfill the independent problem in part 5
    #new input source work for CSV files as part of part 5 of assignment
    frame = pd.read_csv(Path(path))
    if "value" not in frame.columns:
        raise ValueError("CSV must contain a column named value.")
    return frame["value"].tolist()
    
'''

    
