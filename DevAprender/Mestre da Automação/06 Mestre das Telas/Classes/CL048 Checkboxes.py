import PySimpleGUI as psg

psg.theme("DarkGrey13")

layout = [
    [psg.Text("Type a Website")],
    [psg.Input(key="Website")],
    [psg.Text("Do research on which site?")],
    [psg.Checkbox("Google"), psg.Checkbox("Yahoo"), psg.Checkbox("Bing")],
    [psg.Text("Run the program at dawn?")],
    [psg.Radio("Yes", group_id="run_time"), psg.Radio("No", group_id="run_time")],
    {psg.Slider(range=(1, 100), default_value=1, orientation="h")},
    [psg.Button("Send Data", key="Data")],
]

window = psg.Window("Researches", layout)

while True:
    event, value = window.Read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    else:
        print(value)