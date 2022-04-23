import yagmail

user = yagmail.SMTP(user="matheusailvafds@gmail.com", password="46661223")
user.send(to="matheus__.silva@outlook.com", subject="My first e-mail using Python", contents="Hi Matheus! This is my first e-mail using python and yagmail")

# Attachs
user.send(to="matheus__.silva@outlook.com", subject="Data Base", contents="Hi Matheus!\nOpen the attach below...\nAtt.", attachments="Financeiro.xlsx")