# Redo the times table showing a new times table according to user's choice

number = int(input("Type a number that you want a times table: "))
end = int(input("Type a number that you want that will be the and: "))

for c in range(0, end+1):
    print("{} x {} = {}".format(number, c, number * c))