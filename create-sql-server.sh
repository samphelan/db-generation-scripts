#!/bin/bash

docker run --rm -ti -v /Users/samphelan/Documents/charter-ccpa:/home \
    --volumes-from gcloud-config google/cloud-sdk gcloud compute instances create instance-1 \
    --image-family sql-std-2016-win-2016 \
    --image-project windows-sql-cloud \
    --create-disk \
    image=sql-2016-standard-windows-2016-dc-v20191008,image-project=windows-sql-cloud,size=50g,type=pd-standard \
    --zone us-central1-b