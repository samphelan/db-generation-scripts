#!/bin/bash

gcloud config set project labs-sbx

gcloud dataproc clusters create test-cluster \
    --region=global --zone=us-west1-a --worker-machine-type=n1-standard-2 \
    --project labs-sbx

gcloud dataproc jobs submit hive \
    --cluster=test-cluster --file=gs://charter-ccpa/hql-scripts/create-hive-table.hql --region=global