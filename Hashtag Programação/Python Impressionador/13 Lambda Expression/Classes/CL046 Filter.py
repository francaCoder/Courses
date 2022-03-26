tech_prices = {"notebook asus": 2450, "iphone": 4500, "samsung galaxy": 3000, "tv samsung": 1000, "ps5": 3000, "tablet": 1000, "notebook dell": 3000, "ipad": 3000, "tv philco": 800, "notebook hp": 1700}


def over2000(item):
    # if item[1] > 2000:
    #     return True
    return item[1] > 2000


products_over2000 = list(filter(over2000, tech_prices.items()))
print(products_over2000)