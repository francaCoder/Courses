"""
Create a program that should classify products. Each product has a code, all products starting with 'BEB' are alcoholic beverages.
"""

products = ["BEB123", "BEB456", "GRS123", "UKT789", "BEB789", "WEG147", "OIU259", "BEB159", "LSJ844", "QSD753", "BEB862"]

# def is_alcoholic(list):
#     for product in list:
#         if product[:3].upper() == "BEB":
#             print(product)
#
#
# is_alcoholic(products)
# or

def is_alcoholic(drink):
    # for product in list:
    if product[:3].upper() == "BEB":
        return True
    else:
        return False


for product in products:
    if is_alcoholic(product):
        print("Send the product to beverage sector")