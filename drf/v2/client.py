import requests

URL = "http://127.0.0.1:8000/create/student/"

data = {
    "name": "Sohaib Azhar",
    "roll": 95,
    "city": "Rahim Yar Khan"
}

# Use the json parameter to automatically handle JSON encoding
response = requests.post(url=URL, json=data)

# Print the response status and content
print("Status Code:", response.status_code)
print("Response Data:", response.json()) 
