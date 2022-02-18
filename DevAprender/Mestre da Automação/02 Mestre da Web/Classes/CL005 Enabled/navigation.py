from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        # Common methods
        self.driver.get("https://cursoautomacao.netlify.app/") # navigation
        age_field = self.driver.find_element_by_id("campoIdade")
        if age_field.is_enabled():
            print("The field is enabled")
        if age_field.is_enabled() == False:
            print("Field not enabled")



course = AutomateCourse()
course.Start()