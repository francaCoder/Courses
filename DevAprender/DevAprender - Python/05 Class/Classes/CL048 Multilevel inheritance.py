# Simple

class User:
    def __init__(self, name, wage, profession):
        self.name = name
        self.wage = wage
        self.profession = profession

    def employee_register(self):
        print(f"Registering user {self.name}")


class Manager(User):
    def __init__(self, name, wage, profession, sector):
        super(Manager, self).__init__(name, wage, profession)
        self.sector = sector

    def define_sector(self, sector):
        print(f"Defining sector to {sector}")


user1 = User("Camilla", 5000, "Software analyst")
manager = Manager("Roberta", 7000, "Manager", "Project management")


# Multilevel

class Vehicle:
    pass
class Wheels(Vehicle):
    pass
class Car(Wheels):
    pass
class Electric_car(Car):
    pass
class Doors(Electric_car):
    pass
