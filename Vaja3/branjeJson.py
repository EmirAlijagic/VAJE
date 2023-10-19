import json

with open('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.json', 'r') as f:
    deserialized_person = json.load(f)

print(deserialized_person)

deserialized_person['age'] = 40
deserialized_person['married'] = False

with open('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/personUpdated.json', 'w') as f:
    json.dump(deserialized_person, f, indent=4)