import pandas as pd

cars = ["Ferrari", "Rolls Royce", "Bugatti"]

print(pd.Series(cars))

# 0        Ferrari
# 1    Rolls Royce
# 2        Bugatti
# dtype: object

data = [
    {"Car": "Ferrari", "Year": "2022", "Color": "Red"},
    {"Car": "Rolls Royce", "Year": "2020", "Color": "White"},
    {"Car": "Bugatti", "Year": "2023", "Color": "Blue"},
]


cars_df = pd.DataFrame(data)

cars_df = cars_df[["Year", "Color", "Car"]] # Change Order

print(cars_df)
           # Car  Year  Color
# 0      Ferrari  2022    Red
# 1  Rolls Royce  2020  White
# 2      Bugatti  2023   Blue


# External Files

employees_df = pd.read_csv("CadastroFuncionarios.csv", sep=";", index_col=2)
print(employees_df)