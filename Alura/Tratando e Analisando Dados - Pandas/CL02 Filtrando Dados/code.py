import pandas as pd

rent_df = pd.read_csv("aluguel.csv", sep=';')

immobile_type = rent_df['Tipo'] # Or print rent_df.Tipo

# new_df = pd.DataFrame(immobile_type.drop_duplicates())

# print(new_df.index)

immobile_type.index[0] = range(immobile_type.shape[0])
print(immobile_type)