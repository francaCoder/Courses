# Create a code that read a whole number and show on screen your predecessor and successor

mainNumber = int(input("Type a number: "))
preceNumber = mainNumber - 1
sucNumber = mainNumber + 1

print("The number chosen was {}, your predecessor is {} and your successor is {"
      "}".format(mainNumber, preceNumber, sucNumber))

# OR

number = int(input("Type a Number: "))
print(f"The number chosen was {number}, your predecessor is {number - 1} and your successor is {number + 1}")