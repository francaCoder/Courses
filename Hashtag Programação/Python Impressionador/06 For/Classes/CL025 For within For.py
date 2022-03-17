from random import randint

stocks = [
    [randint(000, 999) for c in range(23)],
    [randint(000, 999) for c in range(23)],
    [randint(000, 999) for c in range(23)],
    [randint(000, 999) for c in range(23)],
    [randint(000, 999) for c in range(23)]
]

factories = ["Lira Company", "Matheus Company", "Isa Company", "Gu Company", "Nic Company"]
minimum_level = 50

print(stocks)

companies_below = []
for i, stock in enumerate(stocks):
    for number in stock:
        if number < minimum_level:
            if factories[i] in companies_below:
                pass
            else:
                companies_below.append(factories[i])

print(companies_below)