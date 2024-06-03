import http.client
import json

# Define the server and endpoint
server = "your-server.com"
endpoint = "/register"

# Define file paths
image_path = "path/to/image.jpg"
video_path = "path/to/video.mp4"

# Open and read file data
with open(image_path, 'rb') as image_file:
    image_data = image_file.read()

with open(video_path, 'rb') as video_file:
    video_data = video_file.read()

# Define the request body data
data = {
    'username': 'example_user',
    'email': 'user@example.com',
    'password': 'secure_password',
    'image': image_data,
    'video': video_data
}

# Convert data to JSON format
json_data = json.dumps(data)

# Define headers
headers = {
    'Content-Type': 'application/json',
    'Content-Length': len(json_data)
}

# Connect to the server
conn = http.client.HTTPConnection(server)

# Send POST request
conn.request("POST", endpoint, json_data, headers)

# Get response
response = conn.getresponse()

# Print response status and data
print("Response Status:", response.status)
print("Response Reason:", response.reason)
print("Response Data:", response.read().decode('utf-8'))

# Close connection
conn.close()

