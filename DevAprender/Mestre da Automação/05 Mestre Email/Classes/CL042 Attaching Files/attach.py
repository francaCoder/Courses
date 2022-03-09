import os
import smtplib
from email.message import EmailMessage

import imghdr


email = "matheusautomacaopython@gmail.com"
password = "1597532486a"

# Creating email
msg = EmailMessage()

# Assunto
msg['Subject'] = "Landscapes"

# Remetente
msg['From'] = "matheusautomacaopython@gmail.com"
msg['To'] = "matheus__.silva@outlook.com"

# Content
msg.set_content("Damn, it's amazing! Look at these landscapes,it looks like the heaven...")

# Configure image attachment
images = ['img1.jpg', 'img2.jpg']
for img in images:
    with open(img, 'rb') as file: # Rb - Read binary
        data = file.read()
        ext_img = imghdr.what(file.name) # Find out the extension
        file_name = file.name
    msg.add_attachment(data, maintype='img', subtype=ext_img, filename=file_name)
# Sending
# Safe connection with our e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, password)
    smtp.send_message(msg)