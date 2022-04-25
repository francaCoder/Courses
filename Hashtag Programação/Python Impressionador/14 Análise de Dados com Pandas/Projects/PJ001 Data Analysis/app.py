"""

    * CadastroFuncionarios
    * CadastroClientes
    * BaseServiçosPrestados

What we will do?
We have datas from 2019 about a company of services provision.
1 - total value of payroll: What was the total cost with employees?
    obs - wage + benefits + tax
2 - Company's revenues
3 - Costumers' % that signed a contract
4 - calculate the total number of contracts that each area of the company has already signed
5 - Calculate the total number of employees per area
6 - What's the average monthly ticket of contracts?

"""

# Import

import pandas as pd
import matplotlib.pyplot as mpl
import openpyxl

employees_df = pd.read_csv("CadastroFuncionarios.csv", sep=";", decimal=",")
costumers_df = pd.read_csv('CadastroClientes.csv', sep=";")
services_df = pd.read_excel('BaseServiçosPrestados.xlsx', decimal=",")

#1

print(employees_df.info())

employees_df = employees_df.drop(['Estado Civil', 'Cargo'], axis=1)

# names_wage = []

for i, name in enumerate(employees_df['Nome Completo']):
    print(f"Total cost of {name}: {employees_df['Salario Base'][i] + employees_df['Impostos'][i] + employees_df['Beneficios'][i] + employees_df['VT'][i] + employees_df['VR'][i]}")
    # names_wage.append((name, employees_df['Salario Base'][i] + employees_df['Impostos'][i] + employees_df['Beneficios'][i] + employees_df['VT'][i] + employees_df['VR'][i]))
#
# print(max(names_wage))
# print(min(names_wage))

# 2
revenues_df = services_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(costumers_df[['ID Cliente', 'Valor Contrato Mensal']], on="ID Cliente")
print(revenues_df.info())

for n in revenues_df['ID Cliente']:
    print(n)

revenues_df['Total Revenues'] = revenues_df['Tempo Total de Contrato (Meses)'] * revenues_df['Valor Contrato Mensal']
print(sum(revenues_df['Total Revenues']))


# 3
print(len(employees_df['Nome Completo']))
# -
# valid_ids = []
# contract_signed = 0
# for id in employees_df['ID Funcionário']:
#     valid_ids.append(id)
#
# for id in services_df['ID Funcionário']:
#     if id in valid_ids:
#         contract_signed += 1
#         valid_ids.remove(id)
#
# print(contract_signed)
#
# print(f"The % is → {contract_signed / len(employees_df['ID Funcionário']):.1%}")

# Or

total_employees = len(employees_df['ID Funcionário'])
contract_signed = len(services_df['ID Funcionário'].unique())
print(f"The % is → {contract_signed / total_employees:.1%}")

# 4
contract_area_df = services_df[['ID Funcionário']].merge(employees_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contract_area_df = contract_area_df['Area'].value_counts()
print(contract_area_df)

# 5
employees_area = employees_df['Area'].value_counts()
employees_area.plot(kind='pie')
mpl.show()

# 6
average_ticket = costumers_df['Valor Contrato Mensal'].mean()
print(f"average_ticket → {average_ticket:,.2f}")
