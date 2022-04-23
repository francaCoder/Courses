import pandas as pd
import pyodbc

data_connection = (
    "Driver={SQL Server};"
    "Server=DESKTOP-58SJ061;"
    "Database=ContosoRetailDw;"
)

# Login & password
#UID = login
#PWD = Password

connection = pyodbc.connect(data_connection)
print("Successfully connection")

cursor = connection.cursor()

products_df = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.DimProduct", connection)
print(products_df)