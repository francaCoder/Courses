"""
Navigate to the Google, YouTube and GitHub website and take a screenshot of each one
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time,sleep
import os


websites = [
    "https://www.google.com",
    "https://www.youtube.com/",
    "https://github.com/franssa01"
]
for c in range(0, len(websites)):
    class AutomateCourse:
        def __init__(self):
            chrome_options = Options()
            chrome_options.add_argument('--window-size=1300,800')
            self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
            # self.site = str(input("URL Site for screenshot: "))

        def Start(self):
            self.driver.get(websites[c])
            sleep(2)
            self.save_screenshot()

        def save_screenshot(self):
            file_name = str(round(time() * 1000)) + ".png"
            directory_with_file_name = os.path.join("photos", file_name)
            self.driver.save_screenshot(directory_with_file_name)



    course = AutomateCourse()
    course.Start()