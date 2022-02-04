from datetime import datetime

def line():
    print("-"*30)


def depositing_money():
    print("Depositing money")

    def depositing_dollar():
        line()
        print("Depositing dollar")

    def depositing_real():
        line()
        print("Depositing real")

    depositing_dollar()
    depositing_real()


depositing_money()



def father(number):
    def son_1():
        print("I'm the first son.")


    def son_2():
        print("I'm the second son.")
    if number == 1:
        return son_1


print()


result = father(1)
result()


def my_decorator(function):
    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper()


@my_decorator
def congratulate():
    print("Congratulations!!")


congratulate()

# @my_decorator
# result = my_decorator(congratulate)
# result()