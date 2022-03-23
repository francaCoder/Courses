import matplotlib.pyplot as plt
from random import randint
import numpy as np

# Graphic → line

sales = np.random.randint(1000, 3000, 50)
months = np.arange(1, 51)

# Graphic editions
# plt.plot(months, sales, "-.", color="red")

# Bars

plt.bar(months, sales)
plt.axis([0, 50, 0, max(sales) + 200])
plt.show()

# More graphics

plt.figure(1) #, figsize=()
plt.subplot(1, 3, 1)
plt.plot(months, sales, color="red")
plt.subplot(1, 3, 2)
plt.scatter(months, sales)
plt.subplot(1, 3, 3)
plt.bar(months, sales)
plt.show()