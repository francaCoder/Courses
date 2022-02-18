from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time
import os


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        self.save_screenshot()

    def save_screenshot(self):
        file_name = str(round(time() * 1000)) + ".png"
        directory_with_file_name = os.path.join("photos", file_name)
        self.driver.save_screenshot(directory_with_file_name)


course = AutomateCourse()
course.Start()