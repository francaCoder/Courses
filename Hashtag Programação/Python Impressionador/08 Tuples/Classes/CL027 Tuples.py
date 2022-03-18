# Tuples ar immutables

informations = "Matheus", "00/00/2022", "00/20/2022", 2000, "Employee"
print(informations)

name = informations[0]
was_born = informations[1]
number = informations[3]

print(name, was_born, number)

# OR
# Unpacking

name, was_born, birthday, number, office = informations

#

sales = [100, 200, 300, 400, 500]
employees = ["João", "Matheus", "Lucas", "Bruno", "Pedro"]

for i, sale in enumerate(sales):
    # for item in enumerate(sales):
        # print(item) → Tuples (0, 100)
    print(f"{employees[i]} sold {sale} unities")