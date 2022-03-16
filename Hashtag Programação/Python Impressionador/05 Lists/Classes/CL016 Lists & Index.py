products = ["TV", "Cell", "Mouse", "Keyboard", "Tablet"]
sales = ["1000", "1500", "350", "270", "900"]

# Starts from 0
print(products[1]) # Cell

# The arrays have the same size/length
print(f"The {products[0]}'s sales was {sales[0]} unities.")

# Change values
sales[3] = "300"
print(sales)

name = "Matheus"
print(name[0])
print(name[1])

# How to find any index

index = products.index("Keyboard")
print(index)
print(products[index])