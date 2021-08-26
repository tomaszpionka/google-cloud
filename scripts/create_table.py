from google.cloud import bigquery
from google.oauth2 import service_account

# TODO(developer): Set key_path to the path to the service account key file.
key_path = "credentials\service_account_key.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

def create_table(dataset_name, table_name, credentials=credentials):

    # Construct a BigQuery client object.
    client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

    table_id = "{}.{}.{}".format(credentials.project_id, dataset_name, table_name)

    schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]

    table = bigquery.Table(table_id, schema=schema)
    try:
        table = client.create_table(table)  # Make an API request.
        print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))
    
    except:
        print("job failed")
    # [END bigquery_create_table]