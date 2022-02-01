"""
Create a package called UtilitiesCeV that has 2 modules called coin and data.

Transfer all functions used in challenges for the first package and keep everything working
"""

from UtilitiesCeV import coin
from UtilitiesCeV import data


price = data.readMoney("Price: R$")
coin.summary(price, 20, 12)