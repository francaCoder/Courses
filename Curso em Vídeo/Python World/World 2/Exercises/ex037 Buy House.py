"""
Make a code to approve a bank loan for the purchase of a house. Ask the price of house,
the wage of buyer and in how many years he will pay

If the installments are biggest that 30% of the wage of buyer, he will can't buy
"""

from math import ceil

housePrice = float(input("What's the price of house? R$"))
wage = float(input("What's your current wage? R$"))
years = int(input("How many years do you plan on paying for this house? "))

installments = housePrice / (years * 12)
maximum = wage * 30 / 100

print("For buy a house that cost {} in {} years, you need pay R${} per month...".format(housePrice, years, ceil(installments)))
if installments <= maximum:
    print("Sign the contract and welcome to your new house!")
else:
    print("Sorry, you can't buy this house")


