# coding=utf8
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


df = pd.read_excel('qweqwe.xlsx')

s = Service(r"C:\Users\ilyx\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

for i in range(len(df)):
    # Получить артикул и ссылку на товар из датафрейма:
    article = df.iloc[i][3]
    url = df.iloc[i][4]
    driver.get(url)


    time.sleep(5)
    k = 1080
    for j in range(10):
        driver.execute_script(f"window.scrollTo(0, {k});")
        time.sleep(1)
        k += 500

    # Сохранить HTML-код страницы в файл с названием артикула:
    with open(f'html/{article}.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

