import pandas as pd

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

df1 = pd.DataFrame(data)

index = ["Line" + str(i) for i in range(3)]

df1 = pd.DataFrame(data, index)

columns = ["Column" + str(i) for i in range(3)]
df1 = pd.DataFrame(data, index, columns=columns)

# print(df1)

# Or

data2 = {
    "Column0": {"Line0": 1, "Line1": 4, "Line2": 7},
    "Column1": {"Line0": 2, "Line1": 5, "Line2": 8},
    "Column2": {"Line0": 3, "Line1": 6, "Line2": 9},
}

df2 = pd.DataFrame(data2)
# print(df2)

data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

df3 = pd.DataFrame(data, index, columns)

df1[df1 > 0] = "A"
df2[df2 > 0] = "B"
df3[df3 > 0] = "C"

datas = pd.concat([df1, df2, df3], axis=1) # axis=1
print(datas)