# Create a program that read the whole number and show on screen if it is Even or Odd

number = int(input("Type a number: "))

if number % 2 == 0:
    print(f"{number} is a Even number")
else:
    print(f"{number} is a Odd number")