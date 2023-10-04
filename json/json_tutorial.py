import json

# Serialization in Python
person: dict = {"name": "John", "age": 30, "city": "New York", "hasChildren": False,
                "titles": ["engineer", "programmer"]}

personJson: str = json.dumps(person, indent=3, sort_keys=True)
print(person)
print(personJson)

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Deserialization in Python
person: dict = json.loads(personJson)  # personJson is string loads stands for load from string
print(person)

with open("person.json", "r") as file: # read json from file, load stands for load from file
    person: dict = json.load(file)
    print(person)
