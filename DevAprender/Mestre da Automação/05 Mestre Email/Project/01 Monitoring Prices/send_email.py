import os
import smtplib
import imghdr
from email.message import EmailMessage
from time import sleep


class ReadEmail:
    def __init__(self, origin_email, password_email):
        self.origin_email = origin_email
        self.password_email = password_email

    def content(self, topic, sender, contact_list, email_content):
        self.msg = EmailMessage()
        self.msg['Subject'] = str(topic)
        self.msg['From'] = str(sender)
        self.msg['To'] = (", ").join(contact_list)
        self.msg.set_content(email_content)

    def attach_image(self, images_list):
        for image in images_list:
            with open(image, 'rb') as file:
                data = file.read()
                file_name = file.name
                self.msg.add_attachment(data, maintype='application', subtype='octet-stream', filename=file_name)

    def send_email(self):
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.origin_email, self.password_email)
            smtp.send_message(self.msg)