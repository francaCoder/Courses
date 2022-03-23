import matplotlib.pyplot as mpl

# Graphics
months_sales = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

mpl.plot(months, months_sales)
mpl.ylabel("Sales")
mpl.xlabel("Months")
mpl.axis([0, 12, 0, max(months_sales) + 500])
mpl.show()