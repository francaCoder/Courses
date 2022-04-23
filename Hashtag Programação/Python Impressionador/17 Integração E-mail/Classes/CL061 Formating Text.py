import yagmail

user = yagmail.SMTP(user="matheusailvafds@gmail.com", password="46661223")

# 1
email_body = [
    "Hi Matheus!",
    "This is my first e-mail using python and yagmail.",
    "Att.,"
    "Matheus"
]

email_body = "\n".join(email_body)

#2
"""
...
"""

#3
#html



user.send(to="matheus__.silva@outlook.com", subject="My first e-mail using Python", contents="Hi Matheus! This is my first e-mail using python and yagmail")