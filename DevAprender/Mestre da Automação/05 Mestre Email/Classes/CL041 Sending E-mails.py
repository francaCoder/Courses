import os
import smtplib
from email.message import EmailMessage


email = "matheusautomacaopython@gmail.com"
password = "1597532486a"

# Creating email
msg = EmailMessage()

# Assunto
msg['Subject'] = "Your shirt arrived"

# Remetente
msg['From'] = "matheusautomacaopython@gmail.com"
msg['To'] = "matheus__.silva@outlook.com"

# Content
msg.set_content("Hi, your t-shirt arrived now, came withdraw.")

# Sending
# Safe connection with our e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)