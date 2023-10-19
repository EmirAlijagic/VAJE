import json

person = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "Dunajska",
        "city": "Ljubljana"
    },
    "married": True
}

with open('C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.json', 'w') as f:
    json.dump(person, f, indent=4, sort_keys=True)