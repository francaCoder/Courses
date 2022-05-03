import pandas as pd

data = pd.read_csv("alugueis_residenciais.csv", sep=';')

print(data.info())
data = data[['Valor', 'Condominio', 'IPTU', 'Area', 'Tipo']].fillna(0)

data['Valor Bruto'] = data['Valor'] + data['Condominio'] + data['IPTU']

# print(data[['Valor Bruto', 'Valor', 'Condominio', 'IPTU']].head(10))

data['Valor m2'] = data['Valor'] / data['Area']
data['Valor m2'] = data['Valor m2'].round(2)
print(data['Valor m2'])

print(data[['Valor', 'Condominio', 'IPTU', 'Valor m2', 'Valor Bruto']].head(10))


house = ["Casa", "Casa de Condominio", "Casa de Vila"]

data['Tipo Agregado'] = data['Tipo'].apply(lambda x: "Casa" if x in house else "Apartamento")

data['Valor Bruto m2'] = (data['Valor'] + data['Condominio'] + data['IPTU']) / data['Area']
data['Valor Bruto m2'] = data['Valor Bruto m2'].round(2)
# Remove IPTU

new_data = data[["Tipo Agregado", "Valor m2", "Valor Bruto", "Valor Bruto m2"]]

#1
# del new_data['Valor Bruto']

#2
# new_data.pop('Valor Bruto m2')

#3
new_data.drop(["Valor Bruto", "Valor Bruto m2"], axis=1, inplace=True)
print(new_data)

new_data.to_csv("aluguel_residencial.csv", sep=';', index=False)