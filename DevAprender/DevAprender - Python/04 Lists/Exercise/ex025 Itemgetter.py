"""
Sort the product's list below in ascending order according to the price:
"""

from operator import itemgetter

products = [
    {
        "Name": "Cell",
        "Price": 1500
    },
    {
        "Name": "Monitor",
        "Price": 1000
    },
    {
        "Name": "tv",
        "Price": 2000
    },
]

products.sort(key=itemgetter('Price'))
print(products)


# 2
# Order in ascending order the filming_equipment's list below, according to the equipment's price:

filming_equipment = [
    ("Tripod", 300),
    ("Camera", 1700),
    ("Ring light", 500),
]


filming_equipment.sort(key=itemgetter(1))
print(filming_equipment)


# 3 Order in ascending order the price_coin, according to coin's price:

price_coin = [["USD", 1], ["BRL", 0.19], ["EUR", 1.45]]

price_coin.sort(key=itemgetter(1))
print(price_coin)