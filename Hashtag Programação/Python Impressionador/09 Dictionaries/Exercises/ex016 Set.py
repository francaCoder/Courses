# Set
# Remove duplicate values

set_products = {"Rice", "Beans", "Fish", "Egg", "Milk"}
print(set_products) # show values in random order

cpf_customers = ["278.435.020-76", "961.600.060-88", "754.361.170-82", "595.953.570-06", "731.080.710-33", "961.600.060-88", "595.953.570-06"]

print(len(cpf_customers)) # 7

# print(len(set(cpf_customers))) # 5

print(f"We have {len(set(cpf_customers))} customers in our store")