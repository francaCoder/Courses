"""
Using the zip_longest, the result should be:
{ for each product print:
    product {c}: R${price}
}
"""

from itertools import zip_longest

products = ["Product1", "Product2", "Product3", "Product4", "Product5"]
prices = ["R$550,00", "R$1500,00", "R$2700,00", "R$5000,00"]

for product, price in zip_longest(products, prices):
    if price == None:
        print(f"{product} without price.")
    else:
        print(f"{product}: {price}")