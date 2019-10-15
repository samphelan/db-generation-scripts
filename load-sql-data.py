import pyodbc
import random
from faker import Faker

cnxn = pyodbc.connect(
    driver='{ODBC Driver 13 for SQL Server}', server='35.193.67.115', uid='sa', pwd='TestPassword123')
cnxn.autocommit = True
cursor = cnxn.cursor()

cursor.execute("""IF NOT EXISTS 
    (
        SELECT name FROM master.dbo.sysdatabases 
        WHERE name = N'test'
    )
CREATE DATABASE [test]""")
cursor.execute("USE test")
cursor.execute("""IF NOT EXISTS
    (
        SELECT name FROM sys.schemas 
        WHERE name = N'users'
    )
    BEGIN
        EXEC('CREATE SCHEMA users;');
    END;""")
cursor.execute('DROP TABLE users.user_info')
cursor.execute("""IF NOT EXISTS 
    (
        SELECT * FROM sys.tables t 
        JOIN sys.schemas s ON (t.schema_id = s.schema_id)
        WHERE s.name = 'users' AND t.name = 'user_info'
    ) 
CREATE table users.user_info 
    ( 
        user_id INT PRIMARY KEY IDENTITY (1,1),
        first_name VARCHAR(64) NOT NULL,
        last_name VARCHAR(64) NOT NULL,
        phone_number VARCHAR(64),
        address VARCHAR(64),
        is_active CHAR(1)
    )""")

fake = Faker()
for _ in range(1000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = fake.phone_number()
    address = fake.address()
    random_int = random.randint(0, 1)
    if random_int == 0:
        is_active = 'N'
    else:
        is_active = 'Y'
    insert_string = """INSERT INTO users.user_info 
        (first_name, last_name, phone_number, address, is_active)
        VALUES ('{}','{}','{}','{}','{}')""".format(first_name, last_name, phone_number, address, is_active)
    print(insert_string)
    cursor.execute(insert_string)
