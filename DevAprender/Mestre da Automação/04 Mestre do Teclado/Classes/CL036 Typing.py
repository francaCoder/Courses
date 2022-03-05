from time import sleep
import pyautogui
import pyperclip
from mouseinfo import mouseInfo

# Pyperclip = Brazilian characters

# pyautogui.moveTo(x=1500, y=400, duration=1)
# pyautogui.click()

# pyautogui.typewrite("Automation Example")

# pyautogui.press('') → One Key
# pyautogui.hotkey('', '') → combination

phrases = [
    "Phrase1",
    "Phrase2",
    "Phrase3",
]
while True:
    pyautogui.moveTo(x=1500, y=400, duration=1)
    pyautogui.click()
    for phrase in phrases:
        def copy_phrase(phrase):
            pyperclip.copy(phrase)
            pyautogui.hotkey('ctrl', 'v')


        copy_phrase(phrase)
        sleep(1)
        pyautogui.hotkey('end', 'enter')
        sleep(1)

print(mouseInfo())


