import json

python_data = {'name': 'python', 'version': 3.13}

# python object -> json
json_data = json.dumps(python_data)
print("Python Object to JSON: " + json_data)

# json -> python object
parsed_data = json.loads(json_data)
print("JSON to Python Object: " + json_data)
