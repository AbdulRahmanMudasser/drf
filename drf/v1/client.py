import requests

# Take Input
option = int(input("View All Students (1), View Student By ID (2): "))

# What You Want to See
if option == 1:
    BASE_URL = "http://127.0.0.1:8000/queryset"
else:
    id = input("Enter Student Id: ")
    BASE_URL = f"http://127.0.0.1:8000/modelinstance/{id}"

# Send Get Request
request = requests.get(url=BASE_URL)

# Convert Data to JSON
json_data = request.json()

# Print Json Data
print(json_data)