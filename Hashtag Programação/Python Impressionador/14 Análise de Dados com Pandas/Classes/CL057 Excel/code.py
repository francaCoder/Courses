import pandas as pd
from openpyxl import Workbook, load_workbook

table = pd.read_excel("Produtos.xlsx")

print(table.info())

# Loc - Locate (Line - Column)

table.loc[table['Tipo'] == "Serviço", "Multiplicador Imposto"] = 1.5
table['Preço Base Reais'] = table['Multiplicador Imposto'] * table['Preço Base Original']

table.to_excel("Produtos_pandas.xlsx", index=False)

spreed_sheet = load_workbook("Produtos_pandas.xlsx")

active_tab = spreed_sheet.active

# active_tab["A1"] # Line
# active_tab["C"] # Column

for cell in active_tab["C"]:
    # print(item.value)
    if cell.value == "Serviço":
        line = cell.row
        active_tab[f"D{line}"] = 1.5
        print("ok")
    else:
        print("No")


spreed_sheet.save("Produtos_openPy.xlsx")