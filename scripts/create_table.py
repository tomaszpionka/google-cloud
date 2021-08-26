from google.cloud import bigquery
from google.api_core.exceptions import BadRequest, Conflict, NotFound
from authenticate import create_client

# TODO(developer): Set key_path to the path to the service account key file in authenticate.py.

def create_table(dataset_name: str, table_name: str):

    # Call a BigQuery client object contructor.
    client = create_client()

    # Provide schema for your table
    schema = [
        bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
    ]

    table = bigquery.Table("{}.{}.{}".format(client.project, dataset_name, table_name), schema=schema)

    try:
        job = client.create_table(table)  # Make an API request.
        print("Created table {}.{}.{}".format(job.project, job.dataset_id, job.table_id))
    
    except (BadRequest, Conflict, NotFound) as e:
        print('ERROR: {}'.format(e))
    # [END bigquery_create_table]