import PySimpleGUI as psg

psg.theme("DarkGrey13")

# Key → Inside the inputs
layout = [
    [psg.Text("Type your Name:")],
    [psg.Input(key="Name")],
    [psg.Text("Type your Age:")],
    [psg.Input(key="Age")],
    [psg.OK(), psg.Cancel(), psg.Button("Send Data", disabled=True, key="Data"), psg.Text(key="Access")],
]

window = psg.Window("My window", layout)

while True:
    event, values = window.Read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    elif event == "OK":
        print(values['Name'])
        if int(values['Age']) >= 18:
            window['Access'].update("Allowed access.")
            window['Data'].update(disabled=False)
        else:
            window['Access'].update("Access denied.")
            window['Data'].update(disabled=True)
            window['Age'].update(text_color='red')