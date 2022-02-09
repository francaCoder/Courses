class computer:
    operational_system = "Windows 10"


    def __init__(self, brand, ram, motherboard):
        self.brand = brand
        self.ram = ram
        self.motherboard = motherboard

    def display_computer_data(self):
        print(f"Computer's brand → {self.brand}\nRam → {self.ram}\nMotherboard → {self.motherboard}")

    @classmethod
    def computer_office(cLs, ram):
        return cLs("Dell", ram, "Cheap motherboard")

    @classmethod
    def computer_heavy_configuration(cLs, ram):
        return cLs("Dell", ram, "Expensive motherboard")

    #Static methods
    @staticmethod
    def runs_heavy_programs(ram):
        if ram >= 8:
            return True
        else:
            return False



# Office
computer1 = computer.computer_office(8)

# Gamer
computer2 = computer.computer_heavy_configuration(32)

computer1.display_computer_data()
print()
computer2.display_computer_data()