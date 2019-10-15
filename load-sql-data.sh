#!/bin/bash

docker run --rm -ti -v /Users/samphelan/Documents/charter-ccpa:/home \
    sql-server-image python /home/load-sql-data.py