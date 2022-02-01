"""
Create a module called coin.py that has built-in functions
increase()
decrease()
double()
half()

Also make a program and import some functions.
"""

import coin


price = float(input("Price $"))
print(f"Half of {price} is {coin.half(price)}")
print(f"Double {price} is {coin.double(price)}")
print(f"Increasing 10%, we have {coin.increase(price, 10)}")
print(f"Decreasing 13%, we have {coin.decrease(price, 13)}")