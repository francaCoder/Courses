import requests
from flask import Flask

# API Micro Site (Django or Flask)
# A Minimal Application

app = Flask(__name__) # Create a website

@app.route("/") # Decorator
def hello_world(): # Function
    return {"Lira": "Teste1"}

@app.route("/liramaroto") # Decorator
def lira(): # Function
    return {"Lira": "Teste2"}

@app.route("/mentolira") # Decorator
def mentolira(): # Function
    return {"Lira": "Teste3", "Turma": "Python Impressionador"}

app.run() # turn on the website

# website = requests.get("http://127.0.0.1:5000/liramaroto")
#
# site = website.json()
# print(site)

# website = requests.get("https://Teste.lirahashtag.repl.co")
#
# site = website.json()
# print(site['faturamento'])