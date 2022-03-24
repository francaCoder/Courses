"""
You are analyzing the products' sales of a company
This list has: (product, sales_2019, sales_2020)
- Create a list only with 'sales_2019'
"""
from pprint import pprint

products_sales = [
    ("iphone", 558147, 951642),
    ("Galaxy", 712350, 244295),
    ("Ipad", 573823, 26964),
    ("tv", 405252, 787604),
    ("grind coffee", 718654, 867660),
    ("Kindle", 531580, 78830),
    ("Freezer", 973139, 710331),
    ("Keyboard", 892292, 646016),
    ("Notebook dell", 422760, 694913),
    ("Notebook hp", 154753, 539704),
    ("notebook asus", 887061, 324831),
    ("Microsoft surface", 438508, 667179),
    ("Webcam", 237467, 295633),
    ("Sound Box", 489705, 725316),
    ("Microphone", 328311, 644622),
    ("Camera canon", 591120, 994303)
]

only_sales_2019 = [sales2019 for product, sales2019, sales2020 in products_sales]
pprint(only_sales_2019)
print(len(only_sales_2019))

# Best Seller
print(max(only_sales_2019))

# Best selling product

best_seller = [(sales2019, product) for product, sales2019, sales2020 in products_sales]
print(max(best_seller))