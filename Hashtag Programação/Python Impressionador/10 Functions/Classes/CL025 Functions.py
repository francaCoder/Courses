numbers = [150, 10, 30, 2000, 90]

numbers.sort() # sort() = function
print(numbers)

# How to create a function:
# def name_function:
#   code

# Create
def register_products():
    product = str(input("Product: "))
    print(f"Product {product.lower()} registered successfully")


# Run
register_products()