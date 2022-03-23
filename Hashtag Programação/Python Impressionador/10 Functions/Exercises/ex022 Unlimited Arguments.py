"""
Creating a products' list
Each sector has a different code. Create a function that can receive a several lists and then your function will create a list that the product oly appears once
"""


january_stock = [("BSA2199", 396), ("PPF5239", 251), ("BSA1212", 989), ("PPF5239", 449)]
february_stock = [("BSA2199", 849), ("PPF5239", 877), ("BSA1212", 336), ("PPF5239", 714)]
march_stock = [("BSA2199", 772), ("PPF5239", 394), ("BSA1212", 409), ("PPF5239", 473)]
april_stock = [("BSA2199", 647), ("PPF5239", 292), ("BSA1212", 551), ("PPF5239", 802)]

def show_products(*lists):
    products = []
    for data in lists:
        for product, stock in data:
            products.append(product)
    products = set(products)
    products = list(products)
    return products


print(show_products(january_stock, february_stock, march_stock, april_stock))

