import pandas as pd

# External Files

employees_df = pd.read_csv("cars.csv", sep=";", index_col=0)

# for item in employees_df:
#     print(item)


# For each employee
# print(list(employees_df.iterrows()))
print(employees_df)

for index, row in employees_df.iterrows():
    # print(row['KM']/ (2022 - row["Year"]))
    if 2022 - row['Year'] > 0:
        employees_df.loc[index, "KM Average"] = f"{row['KM'] / (2022 - row['Year']):.2f}"
    else:
        employees_df.loc[index, "KM Average"] = 0

print()
print()

print(employees_df)
print(employees_df.info())

print(employees_df['KM'].isna())
print()

print(employees_df.query(['KM Average'] == 0))

# df.dropna()