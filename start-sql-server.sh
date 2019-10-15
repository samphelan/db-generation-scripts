#!/bin/bash

docker run --rm -ti -v /Users/samphelan/Documents/charter-ccpa:/home \
    --volumes-from gcloud-config google/cloud-sdk /bin/bash -c \
    "gcloud config set project labs-sbx && gcloud compute instances start instance-1"