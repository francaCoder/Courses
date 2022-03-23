# The 'Return' serves as Break, if your code read the return's line, your program will stop

emails = ["matheus@gmail.com", "carla@gmail.com", "tots@hotmail.com", "andre@yahoo.com.br", "claudio@hotmail.com", "david@outlook.com"]


def filter_emails(emails_list, part_text):
    new_list = []
    for email in emails_list:
        if part_text in email:
            new_list.append(email)
            # return new_list
    return new_list


result = filter_emails(emails, "@yahoo.com")
print(result)