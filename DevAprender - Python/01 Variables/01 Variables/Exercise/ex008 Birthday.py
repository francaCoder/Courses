# Calculate how many days to go your birthday


from datetime import datetime

current_day = datetime.now()
birthday = datetime(2022, 7, 20)
how_many_days = birthday - current_day
print(f"{how_many_days} to my birthday.")