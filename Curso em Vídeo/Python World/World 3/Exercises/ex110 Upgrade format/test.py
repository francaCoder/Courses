"""
Modify the functions in 'coin' so that the functions to accept one more parameter, informing whether the returned value will be formatted or not
"""

import coin


price = float(input("Price R$"))
print(f"Half of {coin.coin(price)} is {coin.half(price, True)}")
print(f"Double {coin.coin(price)} is {coin.double(price, True)}")
print(f"Increasing 10%, we have {coin.increase(price, 10, True)}")
print(f"Decreasing 13%, we have {coin.decrease(price, 13, True)}")