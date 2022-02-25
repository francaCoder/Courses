from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://cursoautomacao.netlify.app")
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(1)
frame1 = driver.find_element_by_xpath("//iframe[@src='https://cursoautomacao.netlify.app/desafios.html']")
driver.switch_to.frame(frame1)

text = driver.find_element_by_xpath("//input[@id='dadosusuario']")
sleep(2)
text.send_keys("Estamos dentro do Iframe")
sleep(1)

driver.switch_to.default_content()

paragraph_field = driver.find_element_by_xpath("//textarea[@placeholder='digite seu texto aqui']")
sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
sleep(1)
paragraph_field.send_keys("De volta na principal")