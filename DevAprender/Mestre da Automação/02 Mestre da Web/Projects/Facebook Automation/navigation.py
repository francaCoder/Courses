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
        # self.facebookLink = "https://www.facebook.com"
        self.email = str(input("Email: "))
        self.password = str(input("Password: "))
        self.text = "Welcome to me! My name's Matheus."

    def Start(self):
        self.Login()
        self.Post(
            "https://www.facebook.com/groups/657344725501925",
        )

    def Login(self):
        email_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@name='email']")
            )
        )
        password_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@name='pass']")
            )
        )
        email_field.click()
        self.type_like_person(self.email, email_field)
        sleep(2)
        password_field.click()
        self.type_like_person(self.password, password_field)
        sleep(2)
        password_field.send_keys(Keys.ENTER)
        try:
            sleep(5)
            self.wait.until(
                expected_conditions.visibility_of(
                    (By.XPATH, "//div[text()='Você deve se conectar para continuar.']")
                )
            )
            self.Login()
        except:
            print("Mão foi necessário fazer o segundo login")
            pass

    def Post(self, group_link):
        self.driver.get(group_link)
        comment_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//p[@class='hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5']")
            )
        )
        sleep(3)
        self.type_like_person(self.text, comment_field)
        sleep(1)
        comment_field.send_keys(Keys.ENTER)

    def type_like_person(self, txt, element):
        for letter in txt:
            element.send_keys(letter)
            sleep(randint(1, 5) / 35)


course = AutomateCourse()
course.Start()