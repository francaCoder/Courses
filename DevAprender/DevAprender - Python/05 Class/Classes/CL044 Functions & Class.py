class computer:
    def __init__(self, brand, ram, motherboard):
        self.brand = brand
        self.ram = ram
        self.motherboard = motherboard

    def connect(self):
        print("Turning on the computer.")

    def disconnect(self):
        print("Turning off the computer.")

    def display_computer_data(self):
        print(f"Computer's brand → {self.brand}\nRam → {self.ram}\nMotherboard → {self.motherboard}")


computer1 = computer("Dell", "32bg", "NVIDIA")
computer1.connect()
computer1.disconnect()
computer1.display_computer_data()
