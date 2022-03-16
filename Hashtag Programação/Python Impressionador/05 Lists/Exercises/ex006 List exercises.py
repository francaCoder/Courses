months = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
sales_1 = [10000, 15000, 20000, 25000, 30000, 35000]
sales_2 = [5000, 12000, 18000, 2000, 9000, 50000]

# What was the best and worst month of the year in sales?
year_sales = sales_1 + sales_2

worst_month = min(year_sales)
best_month = max(year_sales)

print(f"The worst month was {months[year_sales.index(worst_month)]}")
print(f"The best month was {months[year_sales.index(best_month)]}")


# 2

total_revenues = sum(year_sales)
percentage = best_month / total_revenues
print(f"The best month is equal {percentage:.2%} of sales os total revenues")

# Top 3 values

top_sales = []
biggest_number = max(year_sales)
top_sales.append(biggest_number)
# print(top_sales)
year_sales.remove(biggest_number)
biggest_number = max(year_sales)
top_sales.append(biggest_number)
#
year_sales.remove(biggest_number)
biggest_number = max(year_sales)
top_sales.append(biggest_number)

print(top_sales)