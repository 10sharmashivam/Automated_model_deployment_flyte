from flytekit import task
import pandas as pd

@task
def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()  # Drop missing values
    data = data[(data['value'] > 0)]  # Remove rows with 'value' column <= 0
    return data