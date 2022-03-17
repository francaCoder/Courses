for c in range(5):
    print(c)
    print("Matheus")

# Create a code that shows the sales for each product
products = ["Coca", "Pepsi", "Guarana", "Sprite", "Fanta"]
sales = [15000, 12000, 13000, 5000, 250]

for c in range(5):
    print(f"product: {products[c]} / Sales: {sales[c]}")

# 5 = len(products)

for c in range(len(products)):
    print(f"product: {products[c]} / Sales: {sales[c]}")