from pprint import pprint
from time import sleep
import pandas as pd
from selenium import webdriver

# Open
driver = webdriver.Chrome()

driver.get("https://pbdatatrader.com.br/jogosdodia")

sleep(10)

iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

# 2
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

table = driver.find_element_by_xpath(
    "//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]")
data = table.text

list_text = data.split("\n")
# print(list_text)

columns = list_text[:10]
values = list_text[10:]

# print()
# print(columns)
# print(values)

dic = {}

for column in columns:
    dic[column] = []
    for i in range(20):
        dic[column].append(values[i])
    values = values[20:]

# print(dic)

table_df = pd.DataFrame.from_dict(dic)
# print(table_df.info())

# scroll

for c in range(200):
    scroll_position = 250 * c
    driver.execute_script(f"document.getElementsByClassName('bodyCells')[0].scroll(0, {scroll_position})")

    table = driver.find_element_by_xpath(
        "//*[@id='pvExplorationHost']/div/div/exploration/div/explore-canvas/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container[19]/transform/div/div[3]/div/visual-modern/div/div/div[2]/div[1]")
    data = table.text

    list_text = data.split("\n")
    columns = list_text[:10]
    values = list_text[10:]

    dic = {}

    for column in columns:
        dic[column] = []
        for i in range(20):
            dic[column].append(values[i])
        values = values[20:]

    temporary_table = pd.DataFrame.from_dict(dic)
    table_df.append(temporary_table, ignore_index=True)

table_df = table_df.drop_duplicates()
print(table_df)