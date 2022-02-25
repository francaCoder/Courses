from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


class AutomateCourse:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--lang=pt-BR')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)


    def Start(self):
        self.driver.get("https://cursoautomacao.netlify.app/")
        sleep(3)
        home_window = self.driver.current_window_handle
        new_window = self.driver.find_element_by_xpath("//button[text()='Abrir aba']")
        self.driver.execute_script("arguments[0].click()", new_window)
        sleep(5)
        windows = self.driver.window_handles
        for wind in windows:
            print(wind)
            if wind not in home_window:
                self.driver.switch_to.window(wind)
                search_field = self.driver.find_element_by_xpath("//input[@id='senha']")
                # self.driver.execute_script("arguments[0].click()", search_field)
                search_field.click()
                search_field.send_keys("123456789")
                sleep(3)
                self.driver.close()
        # Returning
        self.driver.switch_to_window(home_window)



course = AutomateCourse()
course.Start()