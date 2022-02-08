# brand = str(input("Brand: "))
# memory = int(input("RAM Memory"))
# motherboard = str(input("Motherboard: "))
#
# print(f"Your computer is branded {brand}")
# print(f"Your computer has {memory} RAM Memory")
# print(f"Motherboard's name's {motherboard}")


# Functions


# def computer_informations():
#     brand = str(input("Brand: "))
#     memory = int(input("RAM Memory"))
#     motherboard = str(input("Motherboard: "))
#
#     print(f"Your computer is branded {brand}")
#     print(f"Your computer is branded {brand}")
#     print(f"Motherboard's name's {motherboard}")
#
#
# computer_informations()

# Class

class Computer:
    def __init__(self):
        self.brand = "Asus"
        self.ram = "8gb"
        self.motherboard = "NVIDIA"


computer1 = Computer()
print(computer1.brand)
print(computer1.ram)
print(computer1.motherboard)


# OR
print()

class Computer:
    def __init__(self, brand, ram, motherboard):
        self.brand = brand
        self.ram = ram
        self.motherboard = motherboard


computer1 = Computer("Asus", "8gb", "NVIDIA")
print(computer1.brand)
print(computer1.ram)
print(computer1.motherboard)


print()


class Computer:
    def __init__(self, brand, ram, motherboard):
        self.brand = brand
        self.ram = ram
        self.motherboard = motherboard


computer2 = Computer("Dell", "4gb", "GTX")
print(computer2.brand)
print(computer2.ram)
print(computer2.motherboard)