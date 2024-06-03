import requests
import base64

# Read binary data from a file
with open('path/to/file.jpg', 'rb') as file:
    binary_data = file.read()

# Encode binary data as Base64
base64_data = base64.b64encode(binary_data).decode('utf-8')

# Define JSON payload
data = {
    'binary_data': base64_data
}

# Convert data to JSON format
json_data = json.dumps(data)

# Send POST request with JSON payload
response = requests.post(url, json=json_data)

# Check response
if response.status_code == 200:
    print("Data sent successfully!")
else:
    print("Failed to send data. Status code:", response.status_code)

