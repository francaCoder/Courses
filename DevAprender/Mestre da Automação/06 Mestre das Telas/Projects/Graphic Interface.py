import PySimpleGUI as psg

psg.theme("DarkGrey13")

LICENSE = ["TR84D-TR84D-TR84D", "VI0R-VI0R-VI0R"]

users = [
    {
        "User": "Matheus",
        "Password": "123456789"
    },
    {
        "User": "Maxwell",
        "Password": "987654321"
    }
]

numbers = [c for c in range(11)]

def create_login_page():
    layout = [
        [psg.Text("User:")],
        [psg.Input(key="User")],
        [psg.Text("Password")],
        [psg.Input(key="Password", password_char="*")],
        [psg.Text(key="Status", text_color='red')],
        [psg.Button("Login"), psg.Button("Exit")],
    ]

    return psg.Window("Login Challenge", layout, finalize=True)

def create_license_page():
    layout = [
        [psg.Text("Type your License:")],
        [psg.Input(key="License")],
        [psg.Button("Validate License")],
        [psg.Text(key="Status")],
    ]
    return psg.Window("License Window", layout, finalize=True)

def create_settings_page():
    basic_settings = [
        [psg.Text("Which site do you like to automate?")],
        [psg.Radio("Site 1", group_id="site"), psg.Radio("Site 2", group_id="site"), psg.Radio("Site 3", group_id="site")],
        [psg.Checkbox("Option 1"), psg.Checkbox("Option 2"), psg.Checkbox("Option 3")],
        [psg.Text("How many posts should be made on this site?")],
        [psg.Slider(range=(1, 10), orientation="h")]
    ]

    message_settings = [
        [psg.Multiline("Enter the message the be sent here")],
        [psg.Text("How many messages per day?")],
        [psg.Combo(values=[c for c in range(2, 21, 2)], default_value=2)],
        [psg.Text("Account's Level")],
        [psg.Combo(values=["Bronze", "Silver", "Gold"], default_value="Bronze")],
        [psg.Text("How many sites access per day?")],
        [psg.Spin(values=numbers, initial_value=1)],
    ]

    layout = [
        [psg.Frame("Initial Settings", basic_settings)],
        [psg.Frame("Messages Settings", message_settings)],
        [psg.Button("Start")]
    ]
    return psg.Window("Window Settings", layout, finalize=True)


window1, window2, window3 = create_login_page(), None, None

while True:
    window, event, value = psg.read_all_windows()
    if event in (psg.WIN_CLOSED, None, "Exit"):
        window.close()
        break

    if window == window1 and event == "Login":
        for user in users:
            if user['User'] == value['User']:
                if user['Password'] == value['Password']:
                    window1.hide()
                    window2 = create_license_page()
                    break
            else:
                window1['Status'].update("Invalid Login")

    if window == window1 and event == "Exit":
        window.close()
        break

    if window == window2:
        if value['License'] in LICENSE:
            psg.popup("License Successfully")
            window2.hide()
            window3 = create_settings_page()
        else:
            window2['Status'].update("Invalid License")

    if window == window3 and event == "Start":
        print("Starting...")