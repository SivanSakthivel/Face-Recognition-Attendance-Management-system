import json

import json

json_string = '{"key1": "value1", "key2": "value2", "key3": "value3"}'

# Convert JSON string to a dictionary
data_dict = json.loads(json_string)

# Access and print the dictionary
print(data_dict)