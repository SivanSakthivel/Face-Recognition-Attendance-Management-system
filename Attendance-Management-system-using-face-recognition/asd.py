import requests
import pysolr

# URL of the Solr server
solr_url = "http://localhost:8983/solr/patent_data3"

# URL of the data to import
data_url = "https://api.patentsview.org/patents/query?q={%22_gte%22:{%22patent_date%22:%222007-01-04%22}}&f=[%22patent_number%22,%22patent_date%22,%22patent_title%22]"

# Initialize the Solr client
solr = pysolr.Solr(solr_url, timeout=10)

# Fetch the data from the URL
response = requests.get(data_url)

# Assuming the data is in JSON format, you can extract the documents
documents = response.json()
# print(documents)
# Index the documents into Solr
def flatten_json(json_data, prefix=''):
    flattened_data = {}

    for key, value in json_data.items():
        new_key = f"{prefix}.{key}" if prefix else key

        if isinstance(value, dict):
            flattened_data.update(flatten_json(value, prefix=new_key))
        else:
            flattened_data[new_key] = value

    return flattened_data

# Example JSON data
json_data = documents

# Flatten the JSON data
flattened_data = flatten_json(json_data)

solr.add(flattened_data)

# Commit the changes to make them visible immediately
solr.commit()
