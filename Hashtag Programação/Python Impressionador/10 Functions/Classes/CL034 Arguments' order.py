def my_function(arg1, *args, k="kwarg1", **kwargs):
    pass


# Error

def calculate(*numbers, num1):
    total = 0
    for number in numbers:
        total += number
    total += num1


# print(calculate(5, 6, 1))
print(calculate(5, 6, 1, num1=5))

# TypeError: calculate() missing 1 required keyword-only argument: 'num1'
# All arguments were to *numbers