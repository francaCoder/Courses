products = ["TV", "mac", "Iphone", "Ipad", "Airpods"]

# print(products.remove("Iphone x"))
# ERROR, Iphone X not in list



# Error handling
# remove_product = "Iphone x"
#
# if remove_product in products:
#     products.remove(remove_product)
# else:
#     print("This product don't exist in list")


# Or

try: # looks like IF
    products.remove("Iphone x")
except: # Looks like Else
    print("This product don't exist in list")