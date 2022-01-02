# Read the price of a product and show in console the new price with 5% of discount

price = float(input("Type the price of product: R$"))
discount = price * 5 / 100
newPrice = price - discount
print("With the promotion of 5% this same product cost: R${:.2f}".format(newPrice))


print(108 * 8 / 100)