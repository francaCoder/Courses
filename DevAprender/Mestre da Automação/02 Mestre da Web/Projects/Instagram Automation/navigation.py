from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        arguments = ['--lang=pt-BR', '--disable-notification']
        for arg in arguments:
            chrome_options.add_argument(arg)
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        self.wait = WebDriverWait(
            driver=self.driver,
            timeout=10,
            poll_frequency=1,
            ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ]
        )
        # self.instagramLink = "https://www.instagram.com"
        self.username = str(input("Username: "))
        self.password = str(input("Password: "))
        self.text = f"Testando uma mensagem"

    def Start(self):
        self.Login()

    def Login(self):
        username_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@name='username']")
            )
        )
        password_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@name='password']")
            )
        )
        username_field.click()
        self.type_like_person(self.username, username_field)
        sleep(2)
        password_field.click()
        self.type_like_person(self.password, password_field)
        sleep(2)
        password_field.send_keys(Keys.ENTER)
        sleep(5)
        inbox_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[@class='MWDvN']//div[3]//div//div[2]//a")
            )
        )
        inbox_field.click()

        notifications = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[text()='Agora não']")
            )
        )
        notifications.click()

        chat = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//div[@class='             qF0y9          Igw0E     IwRSH      eGOV_         _4EzTm                                                                           i0EQd                                   ']//div//div//div//div//div[2]//a")
            )
        )
        chat.click()

        # for c in range(5):
        comment = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//textarea[@placeholder='Mensagem...']")
            )
        )
        self.type_like_person(self.text, comment)

        send = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//button[text()='Enviar']")
            )
        )
        send.click()

    def type_like_person(self, txt, element):
        for letter in txt:
            element.send_keys(letter)
            sleep(randint(1, 5) / 35)


course = AutomateCourse()
course.Start()