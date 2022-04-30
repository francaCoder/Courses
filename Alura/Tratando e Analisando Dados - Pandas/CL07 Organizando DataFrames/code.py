import pandas as pd

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

list("321")

new_df = pd.DataFrame(data, list("321"), list("zyx"))
print(new_df)

new_df.sort_index(inplace=True)
print(new_df)

new_df.sort_index(inplace=True, axis=1)
print(new_df)

new_df.sort_values(by="x", inplace=True)
print(new_df)

new_df.sort_values(by="3", inplace=True, axis=1)
print(new_df)