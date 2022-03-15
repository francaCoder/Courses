product = input("Product: ")
category = input("Category: ")
amount = int(input("Amount: "))

if product and category and amount:
    if category == "Drinks":
        if amount < 75:
            print(f"Oder {product} from the purchasing team. We have {amount} on the inventory.")
    elif category == "Cleaning":
        pass

else:
    print("Fill in all fields.")