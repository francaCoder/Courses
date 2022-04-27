import pandas as pd

# External Files

employees_df = pd.read_csv("CadastroFuncionarios.csv", sep=";", index_col=2)

select = employees_df.Area == "Financeiro"
select2 = employees_df['Salario Base'] > 500

print(employees_df[select])

# 2 conditions

print(employees_df[(select) & (select2)])

# OR

employees_df.query('Area' == "Financeiro")