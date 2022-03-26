"""
product = 10%
service = 15%
Royalties = 25%
"""


def calculate_price(price):
    return price * 0.1
def calculate_price(price):
    return price * 0.15
def calculate_price(price):
    return price * 0.25


def calculate_tax(tax):
    return lambda price: price * (1 + tax)


calculate_price_product = calculate_tax(0.1)
calculate_price_service = calculate_tax(0.15)
calculate_price_royalties = calculate_tax(0.25)

print(calculate_price_product(100))
print(calculate_price_service(100))
print(calculate_price_royalties(100))