sales = [
    ("01/01/2020", "Iphone", "Blue", "128gb", 350, 4000),
    ("02/02/2020", "Ipad", "Silver", "128gb", 1500, 4000),
    ("03/03/2020", "Iphone", "Blue", "256gb", 127, 6000),
    ("04/04/2020", "Iphone", "Blue", "256gb", 981, 5000),
    ("05/05/2020", "Ipad", "Silver", "256gb", 397, 4800),
    ("06/06/2020", "Ipad", "Silver", "128gb", 784, 6541),
    ("07/07/2020", "Iphone", "Blue", "256gb", 478, 1569),
    ("08/08/2020", "Ipad", "Silver", "128gb", 874, 5419),
]

# Iphone's revenues in 04/04/2020
print(sales[3][5])

# Unities in 07/07/2020
print(sales[6][4])

for item in sales:
    date, product, color, memory, unities, revenues = item

print(date, product, color, memory, unities, revenues)
