# """
# PS C:\Users\mathe_dr5d6so\PycharmProjects\pythonCodes> py
# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# # >>> import os
# # >>> os.name
# 'nt'
# # >>> os.listdir()
# ['.idea', 'Curso em vídeo', 'DevAprender - Python', 'main.py', 'Mestre da Automação', 'Trash', 'venv']
# # >>>
# # >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
# # >>> os.path.join(os.getcwd() + os.sep + "ticket.pdf")
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes\\ticket.pdf'
# # >>> os.getcwd
# <built-in function getcwd>
# # >>> os.path.join(os.getcwd() + os.sep + "passwords" + os.sep + "passwords.txt")
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes\\passwords\\passwords.txt'
# # >>>
# """

from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path=os.getcwd() + os.sep + 'chromedriver.exe')
driver.get("https://cursoautomacao.netlify.app/")

# Name
ticket_path = os.path.join(os.getcwd() + os.sep + "ticket.pdf")
print(os.path.dirname(ticket_path))
print(os.path.basename(ticket_path))

# # Exist
print(os.path.exists("Example.txt"))
print(os.path.exists("ticket.pdf"))

# PS C:\Users\mathe_dr5d6so\PycharmProjects\pythonCodes> py
# Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> os.name
# 'nt'
# >>> os.listdir()
# ['.idea', 'Curso em vídeo', 'DevAprender - Python', 'main.py', 'Mestre da Automação', 'Trash', 'venv']
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
# >>> os.chdir('..')
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects'
# >>> os.chdir('..')
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so'
# >>> os.chdir('PycharmProjects')
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects'
# >>> os.chdir('pythonCodes')
# >>> os.getcwd()
# 'C:\\Users\\mathe_dr5d6so\\PycharmProjects\\pythonCodes'
