# dictionary = {
#     "product1": (sales_2019, sales_2020),
#     "product2": (sales_2019, sales_2020),
#     "product3": (sales_2019, sales_2020),
# }
from pprint import pprint

products = ["iphone", "Samsung", "Tv", "ipad"]
sales_2019 = [1500, 12000, 10000, 13000]
sales_2020 = [1896, 48613, 79743, 12347]

# Zip, (sales_2019[0] and sales_2020[0]), (sales_2019[1] and sales_2020[1])....

amount_sales = zip(sales_2019, sales_2020)
print(amount_sales) # <zip object at 0x000002AD37D96F40>

# for item in amount_sales:
#     print(item)
    # (1500, 1896)
    # (12000, 48613)
    # (10000, 79743)
    # (13000, 12347)

products_sales = dict(zip(products, amount_sales))
pprint(products_sales)