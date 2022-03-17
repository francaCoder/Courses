# Enumerate → Allows you sweep the array and save the index

# Just name

employees = ["Matheus", "João", "Maria", "Carla", "Julia", "Isaac"]
for employee in employees:
    print(employee)


# Name and Index
print()

for i, employee in enumerate(employees):
    print(f"{employee} → {i}")



# Create a code that will control the product's stock

minimum_amount = 500

stock = [1200, 300, 800, 1900, 400, 233, 600]
products = ["Coca", "Pepsi", "Soda", "Sprite", "Fanta", "Vodka", "Whisky"]

for i, amount in enumerate(stock):
    if amount < minimum_amount:
        print(f"We need to buy a product: {products[i]}, just {amount} unities")
