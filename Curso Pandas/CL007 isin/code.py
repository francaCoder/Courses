import pandas as pd

df = pd.read_csv("bank.csv", sep=";")

options = ['secondary', 'tertiary']

new_df = df[(df['marital'] == "single") & (df['education'].isin(options))]
print(new_df)