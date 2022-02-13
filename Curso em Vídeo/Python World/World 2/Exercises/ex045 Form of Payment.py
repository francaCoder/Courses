"""
Calculate the amount to be paid considering your normal price and new conditions of
payment:
- 1x cash payment: 10% off
- 1x card payment: 5% off
- Until 2x in card payment: Normal price
_ 3x or more: 20% interest


price = float(input("What's the price? "))
formPayment = str(input("What's the form of payment? Cash or Card? ")).strip().upper()

if formPayment == "CASH":
    print("In 1x cash payment you has 10% off. This same product will cost R${}".format(price - (price * 10 / 100)))

elif formPayment == "CARD":
    installments = int(input("Choose how many installments do you want pay? (Until 6x) "))
    if installments == 1:
        print("1x Card payment you has 5% off")
    elif installments == 2:
        print("With 2x card payment you do haven't discount, normal price.")
    elif installments == 3:
        print("With an interest of 20% the product will cost R${}".format(price + (price * 20 / 100)))
    elif installments == 4:
        print("With an interest of 20% the product will cost R${}".format(price + (price * 40 / 100)))
    elif installments == 5:
        print("With an interest of 20% the product will cost R${}".format(price + (price * 60 / 100)))
    elif installments == 6:
        print("With an interest of 20% the product will cost R${}".format(price + (price * 80 / 100)))
    elif installments > 6:
        print("Please, choose a number below that 6.")
"""

print("{:=^40}".format(" LOJAS FRANÇA "))

price = float(input("What's the price? R$"))
print("""Form of payment
[ 1 ] 1x cash payment - 10% off
[ 2 ] 1x card payment - 5% off
[ 3 ] Until 2x in card payment - Normal price
[ 4 ] 3x or more - 20% interest
""")
option = int(input("Choose your option "))

if option == 1:
    total = price - (price * 10 / 100)
elif option == 2:
    total = price - (price * 5 / 100)
elif option == 3:
    total = price
    installments = total / 2
    print("Your purchase will be slit in 2x times that R${:.2f}".format(installments))
elif option == 4:
    total = price + (price * 20 / 100)
    totalInstallments = int(input("How many installments? "))
    installment = total / totalInstallments
    print("Your purchase will be slit in {}x times that R${:.2f}".format(totalInstallments, installment))

if option > 4:
    total = price
    print("Invalid payment form, try again.")
print("with the promotion, your purchase of R${:.2f} will cost R${:.2f} with the discount".format(price, total))


