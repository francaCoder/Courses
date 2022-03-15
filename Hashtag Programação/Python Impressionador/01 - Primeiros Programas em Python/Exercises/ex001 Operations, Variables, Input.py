"""
Part 01

Create a program that shown the main store indicators in the last year. (Using Variables)

Last year:
coca_cola = 150
pepsi = 130
coca_cola_unity = 1.50
pepsi_unity = 1.50
store_rent = 2500
"""
coca_cola_sales = 150
pepsi_sales = 130
coca_cola_unity = 1.50
pepsi_unity = 1.50
store_rent = 2500

# 1 - What was the pepsi's turnover?
print(pepsi_sales * pepsi_unity)

# 2 - What was the coca's turnover?
print(coca_cola_sales * coca_cola_unity)

# 3 - What was the store's profit?
turnover = coca_cola_sales * coca_cola_unity + pepsi_sales * pepsi_unity
profit = turnover - store_rent
print(profit)

# 4 - What was the store's profit?
print(profit - turnover)

"""
Part 02 - Inputs & Strings

The companies use a Code/ID for each product, for example:
coca = BEB1300543
pepsi = BEB1300545
wine = BAC154BDD1
vodka = BAC17675002

All drinks that starts with 'BEB' are without alcohol
Using the String manipulation, create a program that verify if the drink is alcoholic or not, returning True or False
"""

coca = "BEB1300543"
pepsi = "BEB1300545"
wine = "BAC154BDD1"
vodka = "BAC17675002"

# Without alcohol
print("BAC" in coca)
print("BAC" in pepsi)

# Alcoholic
print("BAC" in wine)
print("BAC" in vodka)

code = input("What's the drink's code? ")
print("BAC" in code)
