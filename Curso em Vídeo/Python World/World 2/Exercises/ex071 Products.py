"""
Make a code that read the name and the price of several products. The program must ask if the user want continue. At the end show:
- The total spent on the purchase
- How many products cost more that R$1000
- What'shortcut the name of the most expensive product
"""

counter = 0

totalSpent = over1000 = expensiveProduct = cheapProduct = 0
cheap = ""

while True:
    print("---- New Product ----".format(counter))
    name = str(input("Product'shortcut Name: "))
    price = float(input("Product'shortcut Price: R$"))
    while price <= 0:
        price = float(input("Product'shortcut Price: R$"))
    register = str(input("Do you want register this product? [Y/N] ")).strip().upper()[0]
    while register not in "YN":
        register = str(input("Do you want register this product? [Y/N] ")).strip().upper()[0]
    if register == "Y":
        counter += 1
        totalSpent += price
        if price > 1000:
            over1000 += 1
        if counter == 1 or price < cheapProduct:
            cheapProduct = price
            cheap = name
    wantContinue = str(input("Do wou want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Do wou want continue? [Y/N] ")).strip().upper()[0]
    print("-"*40)

    if wantContinue == "N":
        break

print("{:-^38}".format(" Program'shortcut End "))
print("The total spent on the purchase was R${:.2f}".format(totalSpent))
print("{} products cost over R$1000".format(over1000))
print("The cheap product was {} that cost R${:.2f}".format(cheap, cheapProduct))



