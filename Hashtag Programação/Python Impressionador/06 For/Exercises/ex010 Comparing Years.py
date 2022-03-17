# Compare the sales for each year and show the raise in %

products = ["Iphone", "Galaxy", "Ipad", "TV", "Coffee Grinder", "Kindle", "Freezer", "Notebook"]

year_2019 = [452115, 148648, 124856, 741852, 852963, 123456, 456789, 963852]
year_2020 = [159786, 483257, 176482, 166549, 994205, 203148, 784561, 785612]

for i, product in enumerate(products):
    if year_2020[i] > year_2019[i]:
        raise_ = year_2020[i] / year_2019[i] - 1
        print(f"{product} sold R${year_2019[i]:,} in 2019 and {product} sold R${year_2020[i]:,} in 2020. Raise → {raise_:.1%}")