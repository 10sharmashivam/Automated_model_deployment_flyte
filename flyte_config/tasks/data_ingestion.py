from flytekit import task
import requests

@task
def ingest_data(api_url: str) -> dict:
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()