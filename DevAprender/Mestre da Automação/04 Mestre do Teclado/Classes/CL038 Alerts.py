import pyautogui

# pyautogui.alert("Let's automate everything!", title="Mestres da Automação", button="OK")

resposta = pyautogui.confirm(text="Gostaria de continuar?", title="Confirmando", buttons=["Sim", "Não", "Concelar"])

if resposta == "Sim":
    print("Apertou sim")

# Receive informations

link = pyautogui.prompt(text="What's the link?", title="Web automation", default="")

# Password
pyautogui.password(text="Type the password", title="Password", default="", mask="*")