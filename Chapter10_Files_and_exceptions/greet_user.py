import json

filename = 'C:\\Users\\orujoh\\Downloads\\Education\\Python\\Chapter10_Files_and_exceptions\\username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
