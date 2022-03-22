# Create
def register_products():
    product = str(input("Product: ")).strip().lower()
    # print(f"Product {product} registered successfully")
    return product


# Run
products_name = register_products()

print(products_name)