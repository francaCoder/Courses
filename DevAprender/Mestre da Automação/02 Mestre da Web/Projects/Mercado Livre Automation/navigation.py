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

    def Start(self):
        self.driver.get("https://www.mercadolivre.com.br/")
        self.SearchFor("Iphone x")

    def SearchFor(self, phrase):
        search_field = self.wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//input[@id='cb1-edit']")
            )
        )
        search_field.click()
        search_field.send_keys(phrase)
        search_field.send_keys(Keys.ENTER)

        self.wait.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.CLASS_NAME, 'price-tag-fraction')
            )
        )

        prices = self.driver.find_elements_by_class_name("price-tag-fraction")
        new_prices = []
        for price in prices:
            if len(price.text) != 3:
                new_prices.append(price.text)
                print(price.text)

        print(f"The cheapest iphone costs → {min(new_prices)}")


        print("Finish")


course = AutomateCourse()
course.Start()