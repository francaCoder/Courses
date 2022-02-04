"""
Examples:
input()
len()
split() ....

Everything that has () after, it's a function.

def function_name():
    commands...

# You can pass 1 or more parameters
"""


def welcome():
    print("Welcome!")


welcome()


def personalized_welcome(name): # name = parameter
    print(f"Welcome, {name}!")


name = str(input("Name: "))
personalized_welcome(name)


def present_place(opening_hours, place="our Store!"): # Optional parameter / standard answer
    print(f"Meet {place}! Opening Hours → {opening_hours}")


# present_place() = "Meet our Store!"
present_place("08:00 - 12:00", "Disney")



# Positional / nominal arguments


def show_price(product_name, price):
    print(f"{product_name} R${price}")


# Positional arguments → show_price(5000, "Iphone") # Error


show_price(product_name="iphone", price=5000)
show_price(price=5000, product_name="iphone")
# Same thing