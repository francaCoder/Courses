months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
try:
    print(months[15]) # IndexError: list index out of range
except IndexError as error:
    print("[ERROR] Please enter a valid index")
    print(error)