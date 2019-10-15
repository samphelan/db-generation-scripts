#!/bin/bash

docker run --rm -ti -v /Users/samphelan/Documents/charter-ccpa:/home \
    --volumes-from gcloud-config google/cloud-sdk /home/hive-docker-commands.sh