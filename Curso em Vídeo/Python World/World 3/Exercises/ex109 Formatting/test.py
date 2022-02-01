"""
Improve the previous code creating a new function called coin() that can show the values with a
formatted monetary value.
"""

import coin


price = float(input("Price R$"))
print(f"Half of {coin.coin(price)} is {coin.coin(coin.half(price))}")
print(f"Double {coin.coin(price)} is {coin.coin(coin.double(price))}")
print(f"Increasing 10%, we have {coin.coin(coin.increase(price, 10))}")
print(f"Decreasing 13%, we have {coin.coin(coin.decrease(price, 13))}")