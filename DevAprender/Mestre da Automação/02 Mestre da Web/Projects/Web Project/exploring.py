# Using the knowledge shown in the course
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver.exe")
# driver.get(str(input("Type the URL to navigate: ")))
driver.get("https://cursoautomacao.netlify.com")

sleep(2)
# https://cursoautomacao.netlify.com

while True:
    print("Choose your page:")
    windows = int(input("""[1] Home
[2] Challenges
[3] Login
Number: """))
    print()

    while windows not in range(1, 4):
        print("Please, choose a number between 1 and 3")
        windows = int(input("Number: "))

    if windows == 1:
        print("Dou you want interact with: ")
        options = int(input("""[1] Radio Buttons
[2] Checkboxes
[3] Dropdowns
[4] Buttons
[5] Paragraph
[6] New windows
[7] Iframe
[8] ActionChains
Number: """))
        while options not in range(1, 9):
            print("Please, choose a number between 1 and 8")
            options = int(input("Number: "))
        if options == 1:
            sleep(1)

            home = driver.find_element_by_xpath("//a[text()='Home']")
            home.click()

            sleep(1)
            print("We have just 3 Radio Buttons in this page.")

            button1 = ActionChains(driver)
            element = driver.find_element_by_xpath("//input[@id='WindowsRadioButton']")
            sleep(1)
            button1.click(element).pause(1).send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ARROW_DOWN).pause(1).perform()

            print("Finish!")
            sleep(1)
            print("Returning....")
            sleep(1)

        elif options == 2:
            print("Here, we have any levels to access, for example:")

            sleep(2)

            for c in range(1, 4):
                div = driver.find_element_by_xpath(f"//section[2]//div//div//div[{c}]//input")
                div.click()
                print(f"{c}º Checkbox")
                sleep(1)
            print("Scrolling...")
            sleep(1)

            driver.execute_script("window.scrollBy(0, 900)")

            sleep(2)

            print("We can also create a dinamic fields")
            sleep(1)
            create_field = driver.find_element_by_id("checkboxgeradorconteudo")
            create_field.click()
            sleep(1)
            new_field = driver.find_element_by_id("inputNovo")
            text = "This is an example..."


            def type_like_person(txt, element):
                for letter in txt:
                    element.send_keys(letter)
                    sleep(randint(1, 5) / 40)


            type_like_person(text, new_field)

            sleep(1)
            print("Finish!")
            sleep(1)
            driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
            print("Returning....")
            sleep(1)
            print("Scrolling...")
            sleep(1)

        elif options == 3:
            sleep(2)
            print("Dropdown com Bootstrap 4 ")
            sleep(0.5)
            print("Opening 'Menu Dropdown'...")
            drop = ActionChains(driver)
            element = driver.find_element_by_id("dropdownMenuButton")
            drop.click(element).pause(1).perform()
            for c in range(1, 4):
                print(f"Item {c}")
                drop.send_keys(Keys.ARROW_DOWN).pause(1).perform()
            drop.click(element).perform()

            sleep(1)
            print()
            print("Next Dropdown...")
            print()
            sleep(1)

            print("Opening classic Dropdown")
            drop = ActionChains(driver)
            element = driver.find_element_by_xpath("//select[@id='paisselect']")
            drop.click(element).pause(1).perform()
            print("Brasil")
            countries = ["Estados Unidos", "Canadá"]
            sleep(0.5)
            for c in range(len(countries)):
                print(f"{countries[c]}..")
                drop.send_keys(Keys.ARROW_DOWN).pause(1).perform()

            drop.click(element).perform()

            sleep(1)
            print()
            print("Next Dropdown...")
            print()
            sleep(1)

            print("Opening Multi Select Dropdown")
            sleep(1)
            colors = ["Verde", "Azul", "Marrom", "Amarelo"]
            for c in range(1, 5):
                color = driver.find_element_by_xpath(f"//select[@id='exemplo-multi-select']//option[{c}]")
                color.click()
                print(f"{colors[c-1]}")
                sleep(1)

            sleep(1)
            print()
            print("Next Dropdown...")
            driver.execute_script("window.scrollBy(0, 1050)")
            print()
            sleep(1)

            print("Opening Hover")
            sleep(1)
            hover = ActionChains(driver)
            element = driver.find_element_by_xpath("//section[4]//div[@class='col-md boxed']//button")
            hover.click(element).pause(1).perform()
            sleep(1)
            for c in range(1, 5):
                drop.send_keys(Keys.ARROW_DOWN).pause(1).perform()
                if c <= 3:
                    print(f"{c}...")


            print("Finish!")
            sleep(1)
            print("Returning....")
            driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
            sleep(1)

        elif options == 4:
            sleep(2)
            driver.execute_script("window.scrollBy(0, 700)")
            sleep(1)

            print("We can open a new page: ")
            home_window = driver.current_window_handle
            new_window = driver.find_element_by_xpath("//button[text()='Abrir Janela']")
            driver.execute_script("arguments[0].click()", new_window)
            sleep(5)
            windows = driver.window_handles
            sleep(2)
            for window in windows:
                print(window)
                if window not in home_window:
                    driver.switch_to_window(window)
                    sleep(2)
                    search_field = driver.find_element_by_xpath("//input[@id='campo_pesquisa']")
                    search_field.click()
                    sleep(1)
                    search_field.send_keys("This is an example...")
                    # text = "This is an example..."
                    # type_like_person(text, search_field)
                    #
                    # def type_like_person(txt, element):
                    #     for letter in txt:
                    #         element.send_keys(letter)
                    #         sleep(randint(1, 5) / 35)
                    sleep(2)
                    driver.find_element_by_id("fazer_pesquisa").click()
                    driver.close()

    elif windows == 2:
        options = int(input("""
            """))

    elif windows == 3:
        options = int(input("""
            """))