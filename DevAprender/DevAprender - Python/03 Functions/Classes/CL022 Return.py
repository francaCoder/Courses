"""
Process Vs Return
if you will need use this value posteriorly - Return
else, use - Print()
"""




def show_price(coin):
    if coin == "USD":
        print(5.5)


show_price("USD")


def get_price(coin):
    if coin == "USD":
        return 5.5


price = get_price("USD")
if price > 5:
    print("Invest in american stocks.")
else:
    print("Unfavorable quote.")