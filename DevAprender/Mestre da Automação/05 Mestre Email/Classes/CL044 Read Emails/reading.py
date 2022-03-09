from imapclient import IMAPClient
import datetime
import email

HOST = "imap.gmail.com"
USERNAME = "matheusautomacaopython@gmail.com"
PASSWORD = "1597532486a"

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    print(server.list_folders())
    server.select_folder("INBOX", readonly=True)
    messages = server.search([u'SINCE', datetime.date(2022, 3, 7)])
    # You can search for:
    # [u'UNSEEN']
    # [u'SMALLER' 500]
    # [b'NOT', b'DELETED']
    # [u'TEXT', u'foo bar', u'FLAGGED', u'baz']
    # [u'SINCE', date(year, month, day)]

    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_msg = email.message_from_bytes(message_data[b'RFC822'])
        print(uid, email_msg.get('From'), email_msg.get('Subject')) # Extract
        if email_msg.is_multipart():
            for part in email_msg.walk():
                if part.get_content_type() == "text/plain":
                    try:
                        body = part.get_payload(decode=True)
                        body = body.decode()
                        print(body)
                    except UnicodeDecodeError as error:
                        body = part.get_payload(decode=True)
                        body = body.decode('latin-1')
                        print(body)

                elif part.get_content_type() == "text/html":
                    continue
