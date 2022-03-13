from selenium import webdriver
import PySimpleGUI as psg
from time import sleep
import threading
import os

# The Lengthy Operation is initialized inside the thread
def LengthyOperation(window, values):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    print(f"Navigating to the Website → {values['Website']}")
    driver.get(values['Website'])
    sleep(10)
    browsed_site = driver.current_url
    driver.quit()
    window.write_event_value("web_automation_finished", browsed_site)

def StartInterface():
    psg.theme("DarkGrey13")

    layout = [
        [psg.Text("Which website should we browse?")],
        [psg.Input(key="Website")],
        [psg.Button("Start"), psg.Button("Stop")]

    ]

    window = psg.Window("Threads", layout)

    thread_web = None
    while True:
        event, values = window.read()
        if event in (psg.WIN_CLOSED, "Exit"):
            window.close()
            break
        elif event == "Start" and thread_web == None:
            # LengthyOperation(window, values)
            thread_web = threading.Thread(
                target=LengthyOperation, args=(window, values,), daemon=True)
            thread_web.start()
        elif event == "web_automation_finished":
            thread_web.join()
            thread_web = None


StartInterface()
