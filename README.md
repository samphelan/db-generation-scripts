# SQL Server/Hive Cluster Creation and Load Scripts

A collection of scripts for creating a SQL Server instance and a Hive cluster running on VM's in GCP as well as loading data into both.

NOTE: All of the `docker run` commands use an absolute path as the host directory. Any .sh file that uses this command will need to be updated to reflect the path on your local machine.

## Quick Start

### Step 1: Copy this repo

`git clone https://github.com/samphelan/db-generation-scripts.git`

### Step 2: Install Docker Images

These scripts rely on two separate Docker images. The first one is just a Docker image with the Google Cloud SDK installed. If you already have the Google Cloud SDK installed or you are working out of Google Cloud Shell, you could also just run the commands directly. Otherwise, run the following commands locally:

1. `docker pull google/cloud-sdk:latest`
2. `docker run -ti --name gcloud-config google/cloud-sdk gcloud auth login`

To install the second Docker image, you will need a service account file for the relevant GCP project. You can get this from the project console or just ask me and I'll send you mine. Put this .json file in the `sql-server-dockerfile` directory and then run the following command in the home directory:

`docker build -t sql-server-image ./sql-server-dockerfile`

### Step 3: Create a SQL server instance

After completing step 2, you can run the following command to create a SQL server instance:

`./create-sql-server.sh`

NOTE: You only need to do this once. After you've created it, you can just "stop" the instance rather than destroying it and it will maintain all of your data without charge. To start the instance up again, run `./start-sql-server.sh`.

### Step 4: Load Data into SQL Server

Run the following command:

`./load-sql-data.sh`

This will call a python script (`load-sql-data.py`) which will load data line by line using the Python library Faker.

### Step 5: Create Hive Cluster and Load Data

The following script creates and loads data into a Hive cluster using Google's managed Dataproc service:

`create-cluster.sh`

NOTE: This script creates an external Hive table and assumes that there is a .csv file in the following directory: `gs://charter-ccpa/dummy-user-data`. I generated a .csv using mockaroo.com. This could easily be updated to use a data generation strategy similar to the SQL Server process.

## Using the databases

I started working on `ticket-parser.py` to parse an incoming ticket and retrieve the data and put it in GCS. However, it is unfinished and very crude.
