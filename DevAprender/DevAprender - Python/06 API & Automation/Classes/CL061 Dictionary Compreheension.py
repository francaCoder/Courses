from pprint import pprint
from random import randint

pprint({i: i for i in range(20)})

#

products = ["Product1", "Product2", "Product3", "Product4"]
pprint({product: 1 for product in products})

#

pprint({product: [0 for i in range(5)] for product in products})

# or
# Multiple values
print("2 * i")
pprint({product: [2 * i for i in range(5)] for product in products})

# Random
print("Randint")
pprint({product: [randint(0, 9) for i in range(5)] for product in products})