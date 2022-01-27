
persons = {"Name": "Matheus", "Age": 18, "Gender": "M"}
# Values = "Matheus", "18", "M"
# Keys = "Name", "Age", "Gender"
# Items = Keys and Values
print(persons) # {'Name': 'Matheus', 'Age': 18, 'Gender': 'M'
# print(persons[0]) ERROR   -  I haven't persons[0]
print(persons["Name"])
print(f"{persons['Name']} is {persons['Age']} years old.")  # Simples / Double quotes

print(persons.keys())
print(persons.values())
print(persons.items())


for key in persons.keys():
    print(key)

for value in persons.values():
    print(value)

for key, value in persons.items():
    print(f"{key} = {value}")


# I can del a property/key using - del persons[key]
# I can redeclare values

persons["Name"] = "França"
print(persons["Name"]) # "França"

# I can add elements

persons["Weight"] = 84
print(persons.items())

# Lists and Dictionary

brazil = []
state1 = {"state": "Rio de Janeiro", "Abbr": "RJ"}
state2 = {"state": "São Paulo", "Abbr": "SP"}
brazil.append(state1)
brazil.append(state2)

print(brazil) # [{'state': 'Rio de Janeiro', 'Abbr': 'RJ'}, {'state': 'São Paulo', 'Abbr': 'SP'}]
print(brazil[0]) # {'state': 'Rio de Janeiro', 'Abbr': 'RJ'}
print(brazil[1]) # {'state': 'São Paulo', 'Abbr': 'SP'}

# Access properties

print(brazil[0]["state"])
print(brazil[1]["Abbr"])


state = {}
brazil = []
for c in range(0, 3):
    state["state"] = str(input("Federative unit: "))
    state["Abbr"] = str(input("The abbreviation: "))
    brazil.append(state.copy()) # [:] Doesn't work with dictionary
for state in brazil:
    # print(state)
    # {'state': 'Rio', 'Abbr': 'Rj'}
    # {'state': 'Pará', 'Abbr': 'PA'}
    # {'state': 'São Paulo', 'Abbr': 'Sp'}
    for key, value in state.items():
        print(f"The property {key} is → {value}")