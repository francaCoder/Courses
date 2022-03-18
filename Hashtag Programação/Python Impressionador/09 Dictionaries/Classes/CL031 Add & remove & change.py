informations = {}

# Add
# informations['Word'] = "Example"

# Add
# informations.update({"Product": "Iphone", "Value": 4000})

# print(informations)

#

profit_quarter1 = {"Jan": 10000, "Feb": 12000, "March": 90000}
print(profit_quarter1)
profit_quarter2 = {"Apr": 88000, "Mai": 54000, "jun": 9000}

profit_quarter1["Apr"] = 88000

print(profit_quarter1)

# Join

profit_quarter1.update(profit_quarter2)
print(profit_quarter1)


# Modify
# You need assign a new value to a property that already exists

# remove → del
# del "dict_name[prop_name]"

# or .pop()


# dict_name.clear()
# Clear the dictionary