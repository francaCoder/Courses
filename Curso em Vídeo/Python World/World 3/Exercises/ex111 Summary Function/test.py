"""
Create a function that show all functions in coin until this moment
"""

import coin


price = float(input("Price R$"))
print(f"Half of {coin.coin(price)} is {coin.half(price, True)}")
print(f"Double {coin.coin(price)} is {coin.double(price, True)}")
print(f"Increasing 10%, we have {coin.increase(price, 10, True)}")
print(f"Decreasing 13%, we have {coin.decrease(price, 13, True)}")