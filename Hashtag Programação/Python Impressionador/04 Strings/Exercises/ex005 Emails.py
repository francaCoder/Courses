"""
Create a program that will verify:
1 - If the name and email field were filled
2 - If the email contains "@" and if after there is a '.'
"""
name = input("Name: ")
email = input("Email: ")
if name and email:
    if "@" in email:
        index_at = email.find("@")
        server = email[index_at:]
        if "." in server:
            print("Valid Email")
        # if "." in email:
        #     index_stop = email.find(".")
        #     if index_stop > index_at:
        #         print("Valid Email")
        #     else:
        #         print("invalid Email")
        # else:
        #     print("invalid Email")
        else:
            print("Invalid Email")
    else:
        print("invalid Email")
else:
    print("Fill in all fields")