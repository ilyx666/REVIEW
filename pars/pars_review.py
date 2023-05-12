# coding=utf8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import json


with open(r"C:\Users\ilyx\Desktop\rewiew_href.json", "r") as f:
    review_dict = json.load(f)
for a, h in review_dict.items():
    print(a)
    s = Service(r"C:\Users\ilyx\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get(url=h)

    time.sleep(5)
    k = 1080
    for j in range(200):
        driver.execute_script(f"window.scrollTo(0, {k});")
        time.sleep(0.5)
        k += 500

    # Сохранить HTML-код страницы в файл с названием артикула:
    with open(fr'C:\Users\ilyx\Desktop\review_html2\{a}.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)


