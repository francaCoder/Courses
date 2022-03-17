# Products and Unities

products = []

while True:
    product = str(input("Product: "))
    if product == "":
        break
    # if not product:
    #   break
    unities = int(input("Unities: "))
    products.append([product, unities])

print(products)