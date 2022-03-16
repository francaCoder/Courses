# + 10% to the book's price

products = ["Computer", "Book", "Tablet", "Cell", "TV", "air conditioning", "alexa", "machine coffee", "Kindle"]

products_inventory = [
    [100, 200],
    [300, 400],
    [500, 600],
    [700, 800],
    [900, 1000],
    [1100, 1200],
    [1300, 1400],
    [1500, 1600],
    [1700, 1800],
]


if "Book" in products:
    book_index = products.index("Book")
    products_inventory[book_index][1] *= 1.1 # 10%
    print(f"{products_inventory[book_index][1]:.2f}")
