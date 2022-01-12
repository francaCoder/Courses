"""
Make a code that have a tuple fully filled with a count in full starts from zero to twenty
Your program will must read a number from the keyboard (0-20) and show it in full
"""

numbers = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen", "Twenty")

# while True:
#     number = int(input("Type a number between 0 and 20 to see this number written in full: "))
#     if 0 <= number <= 20:
#         break
#     print("Try again. ", end="")

while True:
    number = int(input("Type a number between 0 and 20 to see this number written in full: "))
    while number > 20 or number < 0:
        number = int(input("Type a number between 0 and 20 to see this number written in full: "))
    print(f"You typed the number {numbers[number]}.")
    wantContinue = str(input("Dou you want continue? [Y/N] ")).strip().upper()[0]
    while wantContinue not in "YN":
        wantContinue = str(input("Dou you want continue? [Y/N] ")).strip().upper()[0]
    if wantContinue == "N":
        break



