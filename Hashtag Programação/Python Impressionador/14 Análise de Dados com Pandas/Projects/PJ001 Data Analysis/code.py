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
costumers_df = pd.read_csv("CadastroClientes.csv", sep=";", decimal=",")
services_df = pd.read_excel("BaseServiçosPrestados.xlsx")


# Treatment
# Delete columns ("Estado Civil" e "Cargo")
# axis=0 → Line
# axis=1 → Column

employees_df = employees_df.drop(['Estado Civil', "Cargo"], axis=1)
print(employees_df.info())

# 1

# Create Column
employees_df['Salario Total'] = employees_df["Salario Base"] + employees_df["Impostos"] + employees_df["Beneficios"] + employees_df["VT"] + employees_df["VR"]
print(f"Monthly Payroll → {sum(employees_df['Salario Total']):,}")


# 2
# new spread_sheet

revenues_df = services_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(costumers_df[['Valor Contrato Mensal', 'ID Cliente']], on="ID Cliente")
revenues_df['Faturamento Total'] = revenues_df['Tempo Total de Contrato (Meses)'] * revenues_df['Valor Contrato Mensal']
print(revenues_df.info())
print(f"Total Billing → {sum(revenues_df['Faturamento Total']):,}")

# 3

total_employees = len(employees_df['ID Funcionário'])
contract_signed = len(services_df['ID Funcionário'].unique())
print(f"The % is → {contract_signed / total_employees:.1%}")

# 4
contract_area_df = services_df[['ID Funcionário']].merge(employees_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contract_area_df = contract_area_df['Area'].value_counts()
print(contract_area_df)

# 5
employees_area = employees_df['Area'].value_counts()
print(employees_area)
mpl.plot(employees_area)
mpl.show()

# 6
average_ticket = costumers_df['Valor Contrato Mensal'].mean()
print(f"average_ticket → {average_ticket:,.2f}")