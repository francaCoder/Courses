import pandas as pd

data = [1, 2, 3, 4, 5]

s = pd.Series(data)

print(s)

index = ["Line" + str(i) for i in range(5)]
print(index)

s = pd.Series(data, index)

print(s)

data = {"Line" + str(i): i+1 for i in range(5)}
print(data)

s = pd.Series(data)
print(s)