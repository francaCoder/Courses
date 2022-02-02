# Random values with the library random

import random

print(random.random()) # 0.0 - 1.0
print(random.uniform(5, 10)) # Float number between 5 - 10
print(random.randint(1, 10)) # Int number between 1 - 10

colors = ["Red", "Green", "White"]
print(random.choice(colors))
print(random.choices(colors, k=2)) # Two random options

numbers = ["1", "2", "3", "4", "5"]
print(random.shuffle(numbers))
print()