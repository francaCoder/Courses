tech_prices = {"notebook asus": 2450, "iphone": 4500, "samsung galaxy": 3000, "tv samsung": 1000, "ps5": 3000, "tablet": 1000, "notebook dell": 3000, "ipad": 3000, "tv philco": 800, "notebook hp": 1700}


# List comprehension

result = [product * 1.3 for product in tech_prices.values()]
print(result)

# Map
print()

def calculate_price(price):
    return price * 1.3


price_tax = list(map(calculate_price, tech_prices.values()))
print(price_tax)

# Lambda
print()

price_tax2 = list(map(lambda price: price * 1.3, tech_prices.values()))
print(price_tax2)