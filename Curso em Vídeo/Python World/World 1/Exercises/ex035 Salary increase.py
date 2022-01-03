"""
Salary with up to R$1.250,00 will have an increase of 10%
For lower wages have an increase of 15%
"""

wage = float(input("What's the wage of employee? R$"))

if wage > 1250:
    print(wage + (wage * 10 / 100))
else:
    print(wage + (wage * 15 / 100))