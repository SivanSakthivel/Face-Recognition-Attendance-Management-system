import requests
import json
import mysql.connector

# URL of the data to import
data_url = "https://api.patentsview.org/patents/query?q={%22_gte%22:{%22patent_date%22:%222007-01-04%22}}&f=[%22patent_number%22,%22patent_date%22,%22patent_title%22]"

# Fetch the data from the URL
response = requests.get(data_url)

# Assuming the data is in JSON format, you can extract the documents
documents = response.json()

data=documents['patents']

print(data)



# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)

# Create cursor
cursor = connection.cursor()

# Create database
database_name = "patent_db"
cursor.execute(f"CREATE DATABASE {database_name}")

# Switch to the new database
cursor.execute(f"USE {database_name}")

# Create table
create_table_query = """
CREATE TABLE patents_table (
    patent_number VARCHAR(20),
    patent_date VARCHAR(20),
    patent_title VARCHAR(100)
)
"""
cursor.execute(create_table_query)

# Insert values
insert_query = """
INSERT INTO patents_table (name, age, email)
VALUES (%s, %s, %s)
"""
values = ("John Doe", "25", "john@example.com")
cursor.execute(insert_query, data)

# Commit changes and close connection
connection.commit()
connection.close()
