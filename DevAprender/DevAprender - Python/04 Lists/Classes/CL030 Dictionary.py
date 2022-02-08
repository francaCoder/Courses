# Dictionary

"""
Person = {
    "Name":
    "Age":
    "Height":
}
"""

person = {
    "Name": "Matheus",
    "Age": 18,
    "Height": 1.84
}

print(person)
print(person['Name'])
print(person['Age'])
print(person['Height'])

print(person.keys()) # All properties
print(person.values()) # All values
print(person.items()) # All