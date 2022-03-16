email = "Matheus@hotmail.com"

print("My email is {:<30}, ok?".format(email))
# 30 characters left-aligned

print("My email is {:>30}, ok?".format(email))
# 30 characters right-aligned

print("My email is {:^30}, ok?".format(email))
# 30 characters middle-aligned


# Thousands separator
cost = 500
revenues = 270
profit = revenues - cost
print("The revenues was {:+} and the profit was {:+}".format(revenues, profit))


cost = 5000
revenues = 2700
profit = revenues - cost
print("The revenues was {:,} and the profit was {:,}".format(revenues, profit))


margin = profit / revenues
print("The profit's margin was {:.2%}".format(margin))


print("The revenues was {:,.2f} and the profit was {:,.2f}".format(revenues, profit))


number = 3.4105
print(round(number))