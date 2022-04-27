# Navigate to website - Investing.com and download the SpreadSheet

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()

driver.get("https://br.investing.com/currencies/usd-brl-historical-data")

WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
))

terms = driver.find_element_by_xpath("//button[@id='onetrust-accept-btn-handler']")
terms.click()

try:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, "//i[@class='popupCloseIcon largeBannerCloser']")
    ))

    google_close = driver.find_element_by_xpath("//i[@class='popupCloseIcon largeBannerCloser']")
    google_close.click()
except:
    pass
finally:
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@title='Baixar dados']")
    ))

    download_data = driver.find_element_by_xpath("//a[@title='Baixar dados']")
    download_data.click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.XPATH, "//span[contains(text(), 'Fazer login com Google')]")
    ))

    field_email = driver.find_element_by_xpath("//input[@id='loginFormUser_email']").send_keys("matheusailvafds@gmail.com")
    sleep(1.5)
    password_field = driver.find_element_by_xpath("//input[@id='loginForm_password']").send_keys("pythonabc123!")
    sleep(1.5)
    submit = driver.find_element_by_xpath("//div[@id='loginPopup']//a[contains(text(), 'Login')]")
    submit.click()

    WebDriverWait(driver, 40).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@title='Baixar dados']")
    ))

    download_data = driver.find_element_by_xpath("//a[@title='Baixar dados']")
    download_data.click()