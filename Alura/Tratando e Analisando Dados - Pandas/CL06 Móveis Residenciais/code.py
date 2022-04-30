import pandas as pd

data = pd.read_csv("aluguel.csv", sep=";")

print(data['Tipo'].drop_duplicates())

residencial = ["Quitinete", "Casa", "Apartamento", "Cada de Condomínio", "Casa de Vila"]

selection = data['Tipo'].isin(residencial)

data_is_residencial = data[selection]

data_is_residencial.index = [i for i in range(data_is_residencial.shape[0])]

print(data_is_residencial)

data_is_residencial.to_csv("alugueis_residenciais.csv", sep=';', index=False) # No index