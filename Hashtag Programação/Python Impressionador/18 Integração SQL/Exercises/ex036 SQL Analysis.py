"""
Do the relation with SQL and open the table "FactSales" From ContosoRetailDW.
1 - Calculate the company's daily profit
2 - Profit → (Sales Amount - Total Cost - Discount Amount)
3 - Use Groupby
4 - Use matplot
"""

import pandas as pd
import pyodbc

data_connection = (
    "Driver={SQL Server};"
    "Server=DESKTOP-58SJ061;"
    "Database=ContosoRetailDw;"
)

connection = pyodbc.connect(data_connection)

cursor = connection.cursor()

sales_df = pd.read_sql("SELECT * FROM ContosoRetailDW.dbo.FactSales", connection)
sales_df['Profit'] = sales_df['SalesAmount'] - sales_df['TotalCost'] - sales_df['DiscountAmount']

print(sales_df['Profit'])