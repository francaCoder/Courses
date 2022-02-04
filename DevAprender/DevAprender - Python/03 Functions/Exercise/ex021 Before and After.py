"""
Create a decorator that takes the function passed to it and prints the current time before and after that executing the function.
"""

from datetime import datetime
from time import sleep


def show_time():
    print(f"{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}")


def register(name="<< Unknown >>", surname="<< Unknown >>"):
    print(f"Welcome, {name} {surname}!")

def my_decorator(function):
    show_time()
    print("--- Register ---")
    function()
    sleep(1)
    show_time()
    print("--- Register ---")


my_decorator(register)


#


def monitor_time(function):
    def monitor():
        show_time()
        function()
        show_time()
    return monitor()

@monitor_time
def download_musics():
    print("Downloading songs")


