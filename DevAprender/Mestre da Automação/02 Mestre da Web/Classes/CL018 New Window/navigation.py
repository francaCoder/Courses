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
        sleep(5)
        home_window = self.driver.current_window_handle
        new_window = self.driver.find_element_by_xpath("//button[text()='Abrir Janela']")
        self.driver.execute_script("arguments[0].click()", new_window)
        sleep(5)
        windows = self.driver.window_handles
        sleep(2)
        for window in windows:
            print(window)
            if window not in home_window:
                self.driver.switch_to_window(window)
                search_field = self.driver.find_element_by_xpath("//input[@id='campo_pesquisa']")
                search_field.send_keys("Testando...")
                self.driver.find_element_by_id("fazer_pesquisa").click()
                self.driver.close()
        # Returning
        self.driver.switch_to_window(home_window)



course = AutomateCourse()
course.Start()