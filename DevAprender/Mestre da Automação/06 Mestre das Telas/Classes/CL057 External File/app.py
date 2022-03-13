import PySimpleGUI as psg

psg.theme("DarkGrey13")

layout = [
    [psg.Input(key="File_Path")],
    [psg.FileBrowse("Choose a Files", target="File_Path"), psg.Ok()],
    [psg.Button("Read File")]
]
# Target → Destination path

window = psg.Window("My window", layout)
window.read()

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        window.close()
        break
    elif event == "Read File":
        file_path = values['File_Path']
        with open(file_path, "r") as file_txt:
            for line in file_txt:
                print(line)

# for name in