import requests
import json

# URL of the data to import
data_url = "https://api.patentsview.org/patents/query?q={%22_gte%22:{%22patent_date%22:%222007-01-04%22}}&f=[%22patent_number%22,%22patent_date%22,%22patent_title%22]"

# Fetch the data from the URL
response = requests.get(data_url)

# Assuming the data is in JSON format, you can extract the documents
documents = response.json()

data=documents['patents']

for values in data:
    print(values)