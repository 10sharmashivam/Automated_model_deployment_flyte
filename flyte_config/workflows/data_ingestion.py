from flytekit import task
import requests
import boto3
import pandas as pd

@task
def ingest_data(api_url: str) -> dict:
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

@task
def ingest_data_from_s3(bucket: str, key: str) -> pd.DataFrame:
    s3_client = boto3.client('s3')
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    return df