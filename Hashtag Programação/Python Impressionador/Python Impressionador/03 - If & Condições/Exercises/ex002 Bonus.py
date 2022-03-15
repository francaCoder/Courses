"""
sales goal is 1000.
If the sales is greater or equal to sales goal, the employee will receive 10% of bonus, otherwise the bonus is 0
"""
sales_goal = 1000

employee_1 = 1000
employee_2 = 770
employee_3 = 2700

if employee_1 >= sales_goal:
    print(f"The employee won R${employee_1 * 0.1} of bonus")
if employee_2 >= sales_goal:
    print(f"The employee won R${employee_2 * 0.1} of bonus")
if employee_3 >= sales_goal:
    print(f"The employee won R${employee_3 * 0.1} of bonus")

"""
>= 2000 → 15%
>= 1000 → 10%
< 1000 → 0
"""

employee_1 = 4000

if employee_1 >= 2000:
    print(f"The employee won R${employee_1 * 0.15} of bonus")
elif employee_1 >= 1000:
    print(f"The employee won R${employee_2 * 0.1} of bonus")
else:
    print(f"The employee won R${0} of bonus")