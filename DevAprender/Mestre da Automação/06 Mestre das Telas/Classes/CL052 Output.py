import PySimpleGUI as psg

psg.theme("Reddit")

layout = [
    [psg.Text("Informations")],
    [psg.Output(size=(40, 10))],
    [psg.Input()],
    [psg.Button("Save data")],
]

window = psg.Window("Multiline", layout)

while True:
    event, data = window.read()
    if event == "Save data":
        print(event)
        print(data)
    elif event == psg.WIN_CLOSED:
        window.close()
        break