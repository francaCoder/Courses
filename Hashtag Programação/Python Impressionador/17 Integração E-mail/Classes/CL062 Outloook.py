import win32com.client as win32

# Integration
outlook = win32.Dispatch("outlook.application")

# Create the e-mail
email = outlook.CreateItem(0)

# informations
email.To = "matheusailvafds@gmail.com"
email.Subject = "Python's automatic E-mail"
email.HTMLBody = """
<p>hI França</p>

<p>This is a python code and one automatic e-mail</p>
You need to pay R$15,00</p>

<p>Att,.</p>
<p>Python</p>
"""

email.Send()
print("Finish")