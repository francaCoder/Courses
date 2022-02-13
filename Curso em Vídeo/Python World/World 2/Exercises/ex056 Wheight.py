# Show the biggest and the smallest wheight between 5 peoples

biggest = smallest = 0
for person in range(1, 6):
    weight = float(input("The weight of {}ª person: ".format(person)))
    if person == 1:
        biggest = weight
        smallest = weight
    elif weight > biggest:
        biggest = weight
    elif weight < smallest:
        smallest = weight



print("The biggest weight read was {}Kg.".format(biggest))
print("The smallest weight read was {}Kg.".format(smallest))

# Or

def people(num=0):
    weights = []
    for c in range(0, num):
        weights.append(float(input(f"{c+1}º Person's Weight: ")))
    print(f"The biggest weight read was {max(weights)}Kg.")
    print(f"The smallest weight read was {min(weights)}Kg.")

    
people(5)

# Or


def how_many_people(num=0):
    people = []
    for c in range(0, num):
        person = {
            "Name": str(input("Name: ")),
            "Weight": float(input("Weight: "))
        }
        people.append(person)

    print(people)

    weights = []
    for c in range(0, len(people)):
        weights.append(people[c]['Weight'])

    greater_weight = max(weights)
    less_weight = min(weights)

    print(f"The greater weight was {greater_weight}")
    for c in range(0, len(people)):
        if greater_weight == people[c]['Weight']:
            print(f"{people[c]['Name']} weighs → {greater_weight}")

    print()

    print(f"The less weight was {less_weight}")


how_many_people(3)
