import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Drop missing values
    return df.dropna()