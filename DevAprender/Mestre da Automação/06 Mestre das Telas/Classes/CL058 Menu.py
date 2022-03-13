import PySimpleGUI as psg

psg.theme("DarkGrey13")

menu_homepage = [
    ["Files",
        ["Open", "Save"]],
    ["Edit",
        ["Change image",
            ["Change color", "Change size"],
        "Change Clarity"]],
    ["Help",
        ["Forum"]]
]

layout = [
    [psg.Menu(menu_homepage)],
    [psg.Text("Welcome to my app!")],
    [psg.Output(size=(40, 20))]
]

window = psg.Window("My window", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    elif event == "Change Clarity":
        print("We are changing clarity")