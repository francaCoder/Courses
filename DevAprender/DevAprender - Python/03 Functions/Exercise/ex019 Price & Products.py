"""
Create a function called calculate_values, that receive 2 parameters.
- The first will be the product's price
- The second will be the quantity of products

* The amount must have the default value of 1.
Your function should show the result (price * how many products)
"""

from math import trunc


def calculate_values(price, how_many_products=1):
    print(f"Total → R${trunc(price * how_many_products)},00")


calculate_values(10, 5)

# Or

calculate_values(price=float(input("Price: ")), how_many_products=int(input("How many units: ")))