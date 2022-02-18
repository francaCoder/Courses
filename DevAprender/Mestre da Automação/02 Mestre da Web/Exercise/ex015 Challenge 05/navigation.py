from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(3)
        challenges = self.driver.find_element_by_xpath("//a[text()='Desafios']")
        challenges.click()
        sleep(5)
        checkbox_list = self.driver.find_elements_by_xpath("//section[5]//input[@type='checkbox']")
        clicks = []
        for checkbox in checkbox_list:
            # if checkbox == checkbox_list[1] or checkbox == checkbox_list[3] or checkbox == checkbox_list[4]:
            #     checkbox.click()
            if checkbox != checkbox_list[0] and checkbox != checkbox_list[2]:
                if len(clicks) >= 4:
                    checkbox.click()
                else:
                    clicks.append(checkbox.click())
                    sleep(randint(1, 5) / 30)
        sleep(2)
        text_list = self.driver.find_elements_by_xpath("//section[5]//input[@type='text']")
        for field in text_list:
            field.send_keys("São Paulo")
        sleep(2)
        buttons_list = self.driver.find_elements_by_xpath("//section[5]//button")
        for button in buttons_list:
            if button != buttons_list[2] and button != buttons_list[4]:
                button.click()



course = AutomateCourse()
course.Start()