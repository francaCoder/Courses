from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--window-size=400,1000')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
        # Down and up
        sleep(2)
        self.driver.execute_script("window.scrollBy(200, 0)")
        sleep(2)
        self.driver.execute_script("window.scrollBy(-200, 0)")
        # Positive Number = Right  /  Negative Number = Left
        # 200 = Pixels
        # 1º positive 2º Negative
        # First parameter = pixels(Right / Left)
        # Second parameter = pixels(Down, UP)


course = AutomateCourse()
course.Start()