import pandas as pd

rent_df = pd.read_csv("aluguel.csv", sep=';')

immobile_type = rent_df.Tipo

immobile_type.drop_duplicates(inplace=True)

immobile_type = pd.DataFrame(immobile_type)
immobile_type.index = range(immobile_type.shape[0])

print(immobile_type)

immobile_type.columns.name = "ID"

print(immobile_type)