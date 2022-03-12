import PySimpleGUI as psg

psg.theme("DarkGrey13")

numbers = [c for c in range(1, 101)]

layout = [
    [psg.Text("How many messages per day?")],
    [psg.Slider(range=(1, 100), default_value=1, orientation="h")],
    [psg.Text("Choose a message sending speed")],
    [psg.Spin(values=(numbers), initial_value=1)],
    [psg.Spin(values=("Beginner", "Intermediary", "Advanced"), initial_value="Beginner")],
    [psg.Ok()],
    [psg.Combo(values=["Beginner", "Intermediary", "Advanced"], default_value="Beginner")]
]

window = psg.Window("Spin & Comboboxes", layout)
while True:
    event, value = window.Read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    else:
        print(value)