from datetime import datetime

print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)


# Create a date
apps_launch = datetime(2022, 10, 20)
print(apps_launch)

# I want to receive a date of app's launch
new_apps_launch = datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")), )
print(type(new_apps_launch))

# Difference

current_date = datetime.now()
deadline = new_apps_launch - current_date
print(deadline)