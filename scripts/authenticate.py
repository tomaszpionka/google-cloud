def create_client():
    from google.cloud import bigquery
    from google.oauth2 import service_account

    # TODO(developer): Set key_path to the path to the service account key file.
    key_path = "credentials\service_account_key.json"
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )
    # Construct a BigQuery client object.
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

    return client

if __name__ == "__main__":
    create_client()