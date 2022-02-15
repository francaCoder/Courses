import webbrowser
import threading
from time import sleep

# you can process more than one piece of information at the same time or separate the paths pf your code


def extract_data(site):
    print(f"We are navigating to the site {site}")
    webbrowser.open_new(site)
    for i in range(1, 20):
        print(f"Processing data - {i}/19")
        sleep(1)
    print("Finalizing site data extraction")


def download_files():
    for i in range(1, 10):
        print(f"Downloading files - {i}/10")
        sleep(1)
    print("Downloaded files")


new_thread = threading.Thread(target=extract_data, args=("https:www.devaprender.com",), daemon=True)
new_thread.start()
download_files()
new_thread.join()

# Or

def comment(site):
    print(f"Entering the site: {site}")
    sleep(5)
    print(f"Data processed on the website: {site}")


threads = []
for site in range(100): # 100 Websites
    new_thread = threading.Thread(target=comment, args=(site,))
    threads.append(new_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()