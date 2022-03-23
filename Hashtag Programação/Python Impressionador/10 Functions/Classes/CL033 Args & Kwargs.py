# You can put as many things as you want inside the Print() → def print(self, *args
# *args → as many things as you want

def calculate(*numbers):
    total = 0
    print(numbers)
    for number in numbers:
        total += number
    return total


print(calculate(1, 2, 3, 4, 5, 6, 7, 8, 9))


# **Kwargs

def final_price(price, **additional):
    print(additional)
    if "discount" in additional:
        price *= (1 - additional['discount'])
    if "extra_guarantee" in additional:
        price += additional['extra_guarantee']
    if "tax" in additional:
        price *= (1 + additional['tax'])
    return price


print(final_price(1000, discount=0.1, extra_guarantee=100, tax=0.3, change_color=150))