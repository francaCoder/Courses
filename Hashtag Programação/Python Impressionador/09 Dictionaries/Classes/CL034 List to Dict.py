products = ["iphone", "Samsung", "Tv", "ipad"]
amount_sales = [1500, 12000, 10000, 13000]

# I want my 'products' array to be the keys
dictionary = dict.fromkeys(products, 0) # 0 = Default Value
print(dictionary) # {'iphone': 0, 'Samsung': 0, 'Tv': 0, 'ipad': 0}

tuples_list = [
    ("iphone", 1500),
    ("Samsung", 12000),
    ("Tv", 10000),
    ("ipad", 13000)
]

new_dictionary = dict(tuples_list)
print(new_dictionary)

# or

products = ["iphone", "Samsung", "Tv", "ipad"]
amount_sales = [1500, 12000, 10000, 13000]

new_tuples_list = zip(products, amount_sales)
print(new_tuples_list) # <zip object at 0x0000024FC9BAB580>

# for item in new_tuples_list:
#     print(item)
    # ('iphone', 1500)
    # ('Samsung', 12000)
    # ('Tv', 10000)
    # ('ipad', 13000)

print()
print()


dict_sales = dict(new_tuples_list)
print(dict_sales)

# How much we sold with Tv's?

print(dict_sales['Tv'])