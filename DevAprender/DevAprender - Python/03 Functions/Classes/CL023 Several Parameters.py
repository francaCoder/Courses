def calculate(a, b):
    print(a + b)


def new_calculate(*numbers, b):
    print(numbers)
    for number in numbers:
        b += number
    print(b)


new_calculate(10, 20, 30, b=2)


def several_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)


several_numbers(1, 2, 3, 4, 5, 6)


def sum_list(list):
    even_numbers = 0
    for number in list:
        if number % 2 == 0:
            even_numbers += 1
    print(f"{even_numbers} Even numbers :)")


sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9])