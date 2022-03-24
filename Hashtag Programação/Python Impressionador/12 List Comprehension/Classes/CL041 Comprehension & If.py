goal = 1000
sales = [800, 900, 1000, 1100]
employees = ["Matheus", "Carla", "Tots", "Sabrina"]

# filter

new_list = list(zip(sales, employees))

winners = [employe for sale, employe in new_list if sale >= goal]
print(winners)