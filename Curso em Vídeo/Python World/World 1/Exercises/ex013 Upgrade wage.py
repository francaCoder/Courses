# Read the wage and show the new wage with 15% increase

wage = float(input("How much is your wage? "))
increase = wage + (wage * 15 / 100)

print("With a 15% increase, now you get R${:.2f} per month.".format(increase))