# Payment in cash = 10% Discount
# Payment in installments = 8% increase p/m

price = float(input("Type the price of product: R$"))
promotion = price * 10 / 100
discount = price - promotion
increase = price + (price * 8 / 100)
newIncrease = (increase * 8 / 100)

print("Payment in cash with 10% Discount: {}".format(discount))
print(" ")
print("For payments in installments, have an increase of 8% p/m. This same product would cost:")
print("First month: {:.2f}".format(increase))
print("Second month: {:.2f}".format(increase + newIncrease))
print("Third month: {:.2f}".format(increase + newIncrease * 2))
print("Fourth month: {:.2f}".format(increase + newIncrease * 3))
print("Fifth month: {:.2f}".format(increase + newIncrease * 4))
print("Sixth month: {:.2f}".format(increase + newIncrease * 5))
print("Sixth month: {:.2f}".format(increase + newIncrease * 6))


# OR

price = float(input("Type the product's price: R$"))
promotion = price * 10 / 100
discount = price - promotion
increase = price + (price * 8 / 100)
newIncrease = (increase * 8 / 100)

print(f"Payment in cash with 10% Discount: {discount}")
print()
print("For payments in installments, have an increase of 8% p/m. This same product would cost:")
for c in range(0, 6):
    if c == 0:
        print(f"{c+1}º Month: {increase:.2f}")
    elif c >= 1:
        print(f"{c+1}º Month: {increase + newIncrease * c:.2f}")


