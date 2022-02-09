# polymorphism

print(10 + 20)
print("Hello" + " world!")
# + is polymorphic

class Car:
    def turn_on(self):
        print("Turning on the car")


class Motorcycle:
    def turn_on(self):
        print("Turning on the car")


def start(Vehicle):
    Vehicle.turn_on()


car = Car()
motorcycle = Motorcycle()

start(car)
start(motorcycle)


class Person:
    def presentation(self, name, age=None, gender=None): # None = optional
        if age and gender != None:
            print(f"{name}, {age}, {gender}")
        elif age != None:
            print(f"{name}, {age}")
        elif gender != None:
            print(f"{name}, {gender}")
        else:
            print(f"{name}")


person = Person
person.presentation(name="Matheus", age=18, gender="m")
person.presentation(name="Matheus", age=18)
person.presentation(name="Matheus")
