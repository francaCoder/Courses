class computer:
    operational_system = "Windows 10"


    def __init__(self, brand, ram, motherboard):
        self.brand = brand
        self.ram = ram
        self.motherboard = motherboard

    def connect(self):
        print("Turning on the computer.")


print(computer.operational_system)
# OR
computer.operational_system = "Linux"
# Computer.brand doesn't work
computer = computer("Dell", "32gb", "NVIDIA")
computer.brand = "Asus"
print(computer.brand)