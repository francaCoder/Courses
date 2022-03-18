sales = [
    ("01/01/2022", "Iphone x", 600, 10000),
    ("02/02/2022", "Ipad", 800, 15000),
]

most_seller = ""
unities_seller = 0
for item in sales:
    date, product, unities, revenues = item
    if unities > unities_seller:
        unities_seller = unities
        most_seller = product

print(f"{most_seller} → {unities_seller}")