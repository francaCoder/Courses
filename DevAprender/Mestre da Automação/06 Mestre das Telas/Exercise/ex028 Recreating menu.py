import PySimpleGUI as psg

psg.theme("DarkGrey13")

menu_homepage = [
    ["File",
        ["New File", "Save", "Save-as"]],
    ["Edit",
        ["Size",
            ["Change Resolution", "Change Height", "Change Width"]]],
    ["About",
        ["About Author"]],
]

layout = [
    [psg.Menu(menu_homepage)],
    [psg.Text("Welcome to my app!")],
    [psg.Output(size=(40, 20))]
]

window = psg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    elif event == "About Author":
        print("Created By: França")