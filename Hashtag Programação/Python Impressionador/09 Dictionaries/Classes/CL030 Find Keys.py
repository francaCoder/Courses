best_sellers = {
    "Iphone": 15000,
    "Galaxy": 12000,
    "PS5": 14300,
    "Books": 5400
}

# print(best_sellers['Iphone'])
# print(best_sellers['Galaxy'])
# print(best_sellers['PS5'])

for prop in best_sellers.keys():
    print(prop)

print(best_sellers['Books'])

#

print(best_sellers.get('Books'))

# verify if exist
# if 'property_name' in "dict_name":
#     print("dict_name[property name]")
# If name == None....else....