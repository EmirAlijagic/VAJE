import os
import json
from person_pb2 import Person

file_size = os.path.getsize('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.json')
print(f"JSON file size: {file_size} bytes")

file_size = os.path.getsize('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.pb')
print(f"JSON file size: {file_size} bytes")

with open('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.json', "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {type(value)}")

print("Še za pb")

person_pb = Person()

with open('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.pb', 'rb') as f:
    person_pb.ParseFromString(f.read())


for field, value in person_pb.ListFields():
    print(f"Field: {field.name}, Type: {field.type}, Value: {value}")