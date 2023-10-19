import person_pb2

person = person_pb2.Person()
person.name = "Alice"
person.age = 30
person.street = "Dunajska"
person.city = "Ljubljana"
person.married = True

with open("C:/Users/ea2542/Documents/VAJE/VAJE-3/DATA/person.pb", "wb") as f:
    f.write(person.SerializeToString())