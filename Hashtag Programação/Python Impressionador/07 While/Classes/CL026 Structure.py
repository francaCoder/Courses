# Register products

product = input("Product: ")
products = []

while product != "":
    products.append(product)
    product = input("Product: ")

print(products)