goal = 10000
sales = [
    ("João", 1500),
    ("Julia", 2700),
    ("Marcos", 9900),
    ("Maria", 3700),
    ("Ana", 10300),
    ("Alon", 7070),
]

# Who reached the goal?

for seller in sales:
    # Unpacking
    # name, sale = seller
    # print(name)
    # print(sale)
    if seller[1] > goal:
        print(f"{seller[0]} reached the goal")


for seller, amount in sales:
    if amount > goal:
        print(f"{seller} reached the goal")


# Comparing with the last year. Show the raise in %
# 2021 / 2022

products_sale = [
    ("Iphone x", 1, 10),
    ("Galaxy", 5468, 6789),
    ("Ipad", 1560, 4186),
]

for product, year2021, year2022 in products_sale:
    if year2022 > year2021:
        print(f"{product}, 2021 → {year2021} / 2022 → {year2022} / Raise → {year2022 / year2021 - 1:.0%}")