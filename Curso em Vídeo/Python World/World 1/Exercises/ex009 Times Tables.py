# Show a times tables of some number

number = int(input("Type a number: "))

print("Follow below the times tables: ")
print("-"*12)
print("{} x 1 = {}".format(number, number * 1))
print("{} x 2 = {}".format(number, number * 2))
print("{} x 3 = {}".format(number, number * 3))
print("{} x 4 = {}".format(number, number * 4))
print("{} x 5 = {}".format(number, number * 5))
print("{} x 6 = {}".format(number, number * 6))
print("{} x 7 = {}".format(number, number * 7))
print("{} x 8 = {}".format(number, number * 8))
print("{} x 9 = {}".format(number, number * 9))
print("{} x 10 = {}".format(number, number * 10))
print("-"*12)

# Or


def line(word):
    print(f"-=-=-=-= << {word} >> =-=-=-=-")


def times_table(number=1, times=10):
    line("Times Table")
    for c in range(0, times+1):
        print(f"{number} x {c} = {number * c}")
    line("Finish")


times_table(5, 20)




