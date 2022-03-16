products = ["TV", "mac", "Iphone", "Ipad", "Airpods"]

# Add (at the end)
products.append("new product")
print(products)

# remove
products.pop() # Remove the last index, and you can save this information in a variable
print(products.remove("Airpods")) # Specific


print(len(products))

sales = [1, 2, 3, 5, 6, 7, 8, 4, 9, 10]

# Biggest and Smallest number
print(max(sales))
print(min(sales))


names = ["Matheus", "João", "Douglas"]
ages = [18, 19, 20]

new_list = names + ages
# new_list = names.extend(ages)
print(new_list)


# Order
sales.sort()
print(sales)


# join
print("\n".join(products))


# link lists

list1 = ["Ipad", "Iphone", "Apple tv"]
list2 = list1

print(list1)
print(list2)

list1[1] = "Iphone 11"
print(list1)
print(list2) # Error


names = ["Matheus", "Lucas", "Miguel"]
names2 = names.copy()
# Or names2 = names[:]

print(names)
print(names2)

names[1] = "Gui"

print(names)
print(names2)
