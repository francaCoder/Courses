# list = [expression for item in iterable]


products_prices = [100, 150, 300, 5500]
products = ["ipad", "iphone", "tv", "phone"]

tax = []
for price in products_prices:
    tax.append(price * 0.3)
print(tax)

# Or
print()

tax = [price * 0.3 for price in products_prices]
print(tax)

# Or
print()

def calculate_tax(price, tax):
    return price * tax


tax = [calculate_tax(price, 0.3) for price in products_prices]
print(tax)