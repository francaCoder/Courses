from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        # Find
        login = self.driver.find_element_by_xpath("//a[text()='Login']")
        # Click on Login
        login.click()
        # Find
        email = self.driver.find_element_by_xpath("//input[@id='email']")
        # Click on email field
        sleep(8)
        email.click()
        # Type
        sleep(3)
        email.send_keys("Matheus@hotmail.com")
        # Find
        password = self.driver.find_element_by_xpath("//input[@id='senha']")
        # CLick on password field
        password.click()
        # Type
        sleep(4)
        password.send_keys(123456789)
        # Find
        send = self.driver.find_element_by_class_name("btn.btn-primary")
        # send = self.driver.find_element_by_xpath("//button[text()='enviar']")
        sleep(2)
        send.click()


course = AutomateCourse()
course.Start()