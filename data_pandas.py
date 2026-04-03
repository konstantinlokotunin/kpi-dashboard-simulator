import pandas as pd

def load_data_pandas(filepath):
    df = pd.read_csv(filepath)

    return df
