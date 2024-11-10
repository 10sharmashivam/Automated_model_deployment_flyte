def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    # Example feature extraction
    df['feature'] = df['value'] * 2
    return df