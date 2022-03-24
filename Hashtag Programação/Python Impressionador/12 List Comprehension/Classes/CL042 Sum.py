products = ["coca", "pepsi", "guarana", "skol", "brahma", "agua", "del valle", "dolly", "red bull", "cachaça", "vinho tinto", "vodka", "vinho branco", "tequila", "champagne", "gin", "guaracamp", "matte", "leite de castanha", "leite", "jurupinga", "sprite", "fanta"]

sales = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]

top5 = ["agua", "brahma", "skol", "coca", "leite de castanha"]

# Percentage

total_top5 = 0

for i, product in enumerate(products):
    if product in top5:
        total_top5 += sales[i]

print(f"Top 5: {total_top5/sum(sales):.1%}")

# Or

total_top5 = sum(sales[i] for i, product in enumerate(products) if product in top5)
print(total_top5)
print(f"{total_top5/sum(sales):.1%}")