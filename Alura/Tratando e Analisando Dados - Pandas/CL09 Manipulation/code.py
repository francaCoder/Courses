import pandas as pd

data = [
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16),
]

df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())

print(df)

print(df[['c1', 'c3']])

print(df[1:3][['c1', 'c3']])

print(df[1:2])

print()
print(df.loc['l4'])

print(df.loc['l4', 'c3'])

print(df.iloc[0, 2])

print(df.loc[['l1', 'l4'], ['c3']])
print(df.iloc[[0, 3], [2]])