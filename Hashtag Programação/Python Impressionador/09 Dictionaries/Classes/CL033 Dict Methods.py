sales = {
    "Notebook": "Asus",
    "Iphone": 5000
}

items_sales = sales.items()
print(items_sales)

for item in sales.items():
    product, price = item
    print(item)

# .items()
# .keys() "Notebook", "Iphone"
# .values() "Asus", "5000"