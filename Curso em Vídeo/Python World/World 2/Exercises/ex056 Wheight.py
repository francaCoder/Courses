# Show the biggest and the smallest wheight between 5 peoples

biggest = 0
smallest = 0
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