import requests
from flask import Flask
import pandas as pd

# API Micro Site (Django or Flask)
# A Minimal Application

app = Flask(__name__) # Create a website
employees_df = pd.read_csv("CadastroFuncionarios.csv", sep=';', decimal=',')
print(employees_df.info())

# names = employees_df['Nome Completo']
# print(dict(names).values())

# def all_employees(): # Function
#     names = [name for name in employees_df['Nome Completo']]
#     return {"Employees": names}

# print(all_employees())

@app.route("/") # Decorator
def hello_world(): # Function
    return {"Company": "França"}

@app.route("/allemployees") # Decorator
def all_employees(): # Function
    names = [name for name in employees_df['Nome Completo']]
    return {"Employees": names}

@app.route("/totalwages") # Decorator
def employees_names(): # Function
    total_wages = float(employees_df['Salario Base'].sum())
    return {"Total Wages": total_wages}

@app.route("/employee/total_wage/<employee>") # Decorator
def especific_employee(employee): # Function
    names = [name for name in employees_df['Nome Completo']]
    if employee in names:
        i = names.index(employee)
        total_wage = employees_df['Salario Base'][i] + employees_df['Beneficios'][i] + employees_df['VT'][i] + employees_df['VR'][i]
        return {f"{employee}'s Total Wage": total_wage}
    else:
        return {f"{employee}": "Not Exist"}


app.run() # turn on the website