products = ["BEB123", "BEB456", "GRS123", "UKT789", "BEB789", "WEG147", "OIU259", "BEB159", "LSJ844", "QSD753", "BEB862"]

def is_alcoholic(drink, code_category):
    if product[:3].upper() == code_category:
        return True


for product in products:
    if is_alcoholic(product, "BEB"):
        print(f"Send the product {product} to beverage sector")

    #

    if is_alcoholic(code_category="BEB", drink=product): # Positional argument
        print(f"Send the product {product} to beverage sector")


# Positional Arguments
# drink, code_category
# product, "BEB"