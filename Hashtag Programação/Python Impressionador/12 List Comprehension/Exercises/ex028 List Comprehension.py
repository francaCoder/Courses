products_prices = [2200, 1200, 2400, 50000]
products_name = ["ipad", "iphone", "tv", "house"]

new_list = list(zip(products_prices, products_name))
new_list.sort(reverse=True)
print(new_list)
print()
products = [product for price, product in new_list]
print(products)

# Or

def zip_lists(list1, list2, prices=False, name=False, order=False, reverse_order=False):
    if prices:
        if order:
            new_list = list(zip(list1, list2))
            products = [price for price, product in new_list]
            products.sort()
            return products
        elif reverse_order:
            new_list = list(zip(list1, list2))
            products = [price for price, product in new_list]
            products.sort(reverse=True)
            return products
        else:
            new_list = list(zip(list1, list2))
            products = [price for price, product in new_list]
            return products
    if name:
        if order:
            new_list = list(zip(list1, list2))
            products = [product for price, product in new_list]
            products.sort()
            return products
        elif reverse_order:
            new_list = list(zip(list1, list2))
            products = [product for price, product in new_list]
            products.sort(reverse=True)
            return products
        else:
            new_list = list(zip(list1, list2))
            products = [product for price, product in new_list]
            return products
    else:
        new_list = list(zip(list1, list2))
        products = [product for price, product in new_list]
        return products



print(zip_lists(products_prices, products_name, prices=True, order=True))