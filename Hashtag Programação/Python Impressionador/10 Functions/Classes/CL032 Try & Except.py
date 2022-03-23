
def discover_server(email):
    try:
        position_a = email.index("@")
        server = email[position_a:]
        if "gmail" in server:
            return "gmail"
        elif "hotmail" in server:
            return "hotmail"
        elif "yahoo" in server:
            return "yahoo"
        elif "uol" in server:
            return "uol"
        else:
            return "Server not found"
    except:
        print("The email doesn't have @")
        raise Exception("The email doesn't have @")
    # else:
    #     server = email[position_a:]
    #     if "gmail" in server:
    #         return "gmail"
    #     elif "hotmail" in server:
    #         return "hotmail"
    #     elif "yahoo" in server:
    #         return "yahoo"
    #     elif "uol" in server:
    #         return "uol"
    #     else:
    #         return "Server not found"


print(discover_server(str(input("Email:  "))))