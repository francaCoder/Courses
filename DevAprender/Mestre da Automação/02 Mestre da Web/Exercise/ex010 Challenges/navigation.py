
# Enter the challenges part and find each button, and then check each one if it is enabled or no


from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        # Common methods
        self.driver.get("https://cursoautomacao.netlify.app/desafios.html") # navigation
        # button1 = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios1']//button[1]")
        # button1 = self.driver.find_element_by_id("btn1")
        # button1 = self.driver.find_element_by_class_name("btn.btn-info")

        # button2 = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios1']//button[2]")
        # button2 = self.driver.find_element_by_class_name("btn2.btn.btn-dark")

        # button3 = self.driver.find_element_by_xpath("//section[@class='jumbotron desafios1']//button[3]")
        # button2 = self.driver.find_element_by_class_name("btn2.btn.btn-warning")

        # if button[].is_enabled():
        #     print("Button[] is enabled.")
        # elif button[].is_enabled() == False:
        #     # elif not button1.is_enabled():
        #     print("Button[] not enabled.")



course = AutomateCourse()
course.Start()