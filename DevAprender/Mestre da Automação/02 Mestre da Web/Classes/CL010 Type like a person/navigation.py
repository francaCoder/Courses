from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import randint


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)
        self.text = "Lorem ipsum dolor sit amet. Id omnis unde sit internos dolorem ut quaerat asperiores. Id possimus facilis eos totam sequi qui internos accusamus qui consequatur nihil est debitis velit cum assumenda voluptatem aut quidem repudiandae. Et asperiores corrupti hic minus expedita non dolorem deserunt aut sequi amet et pariatur ullam ex inventore accusantium. Et debitis nobis ad facere quibusdam ut adipisci aliquam et adipisci aliquam sed maxime sunt."


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        paragraph_field = self.driver.find_element_by_xpath("//textarea[@placeholder='digite seu texto aqui']")
        # paragraph_field.send_keys(self.text)
        self.type_like_person(self.text, paragraph_field)

    def type_like_person(self, text, element):
        for letter in text:
            element.send_keys(letter)
            sleep(randint(1, 5) / 30)


course = AutomateCourse()
course.Start()