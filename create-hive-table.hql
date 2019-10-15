CREATE DATABASE IF NOT EXISTS users;

USE users;

CREATE EXTERNAL TABLE IF NOT EXISTS user_info(
    id int,
    first_name string,
    last_name string,
    email string,
    gender string,
    ip_address string
) 
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION 'gs://charter-ccpa/dummy-user-data';
