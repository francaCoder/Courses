tries = 0
while tries < 3:
    print("Try again")
    tries += 1


password = ""
while password != "123456":
    password = str(input("Type your password: "))
print("Welcome")


name = ""
while name == "":
    name = str(input("Name: "))
print(f"Welcome {name}")


time = 0
while time <= 17:
    print(time)
    time += 1
print("It's time to see the sunset.")


counter = 100
while counter >= 0:
    print(counter)
    counter -= 1