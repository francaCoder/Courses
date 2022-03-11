import PySimpleGUI as psg

psg.theme("Reddit")
layout = [
    [psg.Button("Ordinary Button")],
    [psg.Cancel("Cancel")],
    [psg.OK("OK")],
    [psg.Yes("Yes")],
    [psg.No("No")],
    [psg.Quit("Finish")],
    [psg.Exit("Quit/Exit")],
    [psg.CalendarButton("Chade a date", target="target1"), psg.InputText(key="target1", size=(20, 1))],
    [psg.ColorChooserButton("Choose as color", target="target2"), psg.InputText(key="target2", size=(30, 1))],
    [psg.FileBrowse("Choose a file", target="Target3"), psg.InputText(key="Target3", size=(30, 1))],
    [psg.FilesBrowse("Choose a files", target="Target4"), psg.InputText(key="Target4", size=(30, 1))],
    [psg.FolderBrowse("Choose a folder", target="Target5"), psg.InputText(key="Target5", size=(30, 1))],
]

window = psg.Window("My Window", layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        window.close()
    else:
        print(event)
