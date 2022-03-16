sellers = ["Lira", "Matheus", "Diego", "Alon"]
products = ["Ipad", "Iphone"]
sales = [
    [100, 200],
    [300, 400],
    [500, 600],
    [700, 800]
]

"""
How much Matheus sold of Ipad?
How much Diego sold of Iphone?
What was the total iphone's sales?
"""


print(sales[1][0])
print(sales[2][1])
print(sales[0][1] + sales[1][1] + sales[2][1] + sales[3][1])

# If the Lira only sold 50 Iphones?
sales[0][1] = 50

# new product

sales_mac = [10, 15, 6, 70]

products.append("Mac")

sales[0].append(sales_mac[0])
sales[1].append(sales_mac[1])
sales[2].append(sales_mac[2])
sales[3].append(sales_mac[3])

print(products)
print(sales)