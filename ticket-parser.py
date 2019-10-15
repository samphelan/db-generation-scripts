import yaml
import pyodbc
import time
from google.cloud import dataproc_v1, storage

dataproc_client = dataproc_v1.JobControllerClient()
storage_client = storage.Client()
bucket = storage_client.get_bucket('charter-ccpa')

project_id = 'labs-sbx'
region = 'global'


def generate_query(server):
    query = 'SELECT {} FROM {}.{}'.format(
        server['columns'], server['schema'], server['table'])
    if server['clauses'] == 'none':
        return query
    else:
        return '{} {}'.format(query, server['clauses'])


def query_server(server, query, ip):
    print("query: ", query)
    if server['db-type'] == 'Hive':
        query = """INSERT OVERWRITE DIRECTORY 'gs://charter-ccpa/output' 
        ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' {}""".format(
            query)
        # Define Hive Job config
        query_list = dataproc_v1.types.QueryList(queries=[query])
        hive_job = dataproc_v1.types.HiveJob(query_list=query_list)

        # Define cluster to send Job to
        job_placement = dataproc_v1.types.JobPlacement()
        job_placement.cluster_name = 'test-cluster'

        # Define main Job config
        job = dataproc_v1.types.Job(hive_job=hive_job, placement=job_placement)

        response = dataproc_client.submit_job(project_id, region, job)
        job_id = response.job_uuid
        while(response.status.state == 1):
            response = dataproc_client.get_job(project_id, region, job_id)
            print(response.status.state)
            time.sleep(2)
        print(response)

    elif server['db-type'] == 'SQLServer':
        cnxn = pyodbc.connect(
            driver='{ODBC Driver 13 for SQL Server}', server=ip, database=server['db'], uid=server['uid'], pwd=server['pw'])
        cnxn.autocommit = True
        cursor = cnxn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        row_list = [i for i in rows[0]]
        #blob = bucket.blob('output/sql-data.csv')
        # blob.upload_from_string()
        print(row_list)


with open('/home/ticket.yaml', 'r') as stream:
    try:
        ticket = yaml.safe_load(stream)
        # print(ticket)
        for server in ticket['servers']:
            query = generate_query(ticket['servers'][server])
            query_server(ticket['servers'][server], query, server)

    except yaml.YAMLError as exc:
        print(exc)
