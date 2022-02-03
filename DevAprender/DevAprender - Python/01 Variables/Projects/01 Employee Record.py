"""
Project's goal:
- We are creating a login page in our app, you must get the following information by user:

* - Employee record
1 - User's name
2 - User's age
3 - Automatically register the user registration date
4 - For each employee that is registered in company, he receives one of the following cards:
cards = ["R$50,00","R$250,00","R$120,00"]
5 - Save the informations about the employee's birthday.


* Employee presentation
- With the data obtained in part01, show the following information:
(Welcome, [name], you have been registered successfully on the day [registration date].
  Congratulations, there was a lottery and you won a shopping card worth $[drawn value])
"""

from datetime import datetime
import random


name = str(input("Name: "))
age = int(input("Age: "))
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

registration_date = f"{year}/{month}/{day}"
print("----- Birthday -----")
birthday = datetime.strptime(input("Type your birthday (year/month/day)"), "%Y/%m/%d")
# month = int(input("Month: (Number) "))
# day = int(input("Day: "))
# birthday = [month, day]
print("--------------------")

cards = ["R$50,00", "R$250,00", "R$120,00"]

print(f"Welcome {name}, you have been successfully registered on the day {registration_date}. \n Congratulation, there was a lottery and you won a shopping card worth {random.choices(cards)[0]}.")
