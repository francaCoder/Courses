from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        self.text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"

    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        challenges = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        challenges.click()
        sleep(5)
        paragraph_field = self.driver.find_element_by_xpath("//textarea")
        self.type_like_person(self.text, paragraph_field)


    def type_like_person(self, text, element):
        for letter in text:
            element.send_keys(letter)
            sleep(randint(1, 5) / 30)


course = AutomateCourse()
course.Start()