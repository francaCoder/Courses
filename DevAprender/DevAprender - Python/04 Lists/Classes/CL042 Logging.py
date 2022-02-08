# Logging - Your application history

import logging
"""
debug - Information for developers
info - I just want to report something that happened but it's not an error
warning - I want to alert about something that's unexpectedly happening, but still isn't an error, but it could be in the future 
error - Error
critical - Big mistake
"""
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="a", format='%(levelname)s - %(message)s - %(asctime)s')
# set the level, file name, file mode = append lines ( a )
logging.debug("a")
logging.info("b")
logging.warning("c")
logging.error("D")
logging.critical("Logging critical level")

try:
    email = str(input("Email: "))
    password = int(input("Password: "))
    if password == 1234:
        print("Successfully login")
        logging.info(f"{email} entered your bank account")
except ValueError as error:
    print("Just type numbers")
    logging.info(error)