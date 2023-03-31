# coding=utf8
import pandas as pd
import requests
import lxml
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import undetected_chromedriver
import time
import io
from collections import Counter
from sklearn import preprocessing

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)




nameS = []
brandN = []
pID = []
pHref = []

with open(f"noutbuki.html", encoding='utf-8') as file:
    src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    name = soup.find_all('span', class_='goods-name')
    brand = soup.find_all('span', class_='brand-name')
    product_id = soup.find_all('div', class_='product-card j-card-item')
    hreff = soup.find_all('a', class_='product-card__main j-card-link')

    for i in hreff:
        pHref.append(i.get('href'))


    for i in name:
        nameS.append(i.text.removeprefix(' / '))
    for i in brand:
        brandN.append(i.text)
    for i in product_id:
        pID.append(i.get('id').removeprefix('c'))
    k = 0

    for i in nameS:
        if i[0] != 'Н':
            if i[0] != 'M':
                brandN.pop(k)
                nameS.pop(k)
                pID.pop(k)
                pHref.pop(k)
        k += 1
df = pd.DataFrame({'name': nameS,
                   'brand': brandN,
                    'id': pID,
                   'href': pHref})
br = df.brand.unique()
le = preprocessing.LabelEncoder()
le.fit(df.brand)
df.brand = le.transform(df.brand)
df.to_excel('product.xlsx')
g = df.brand.unique()

df2 = pd.DataFrame({'Brand': br,
                    'id': g})

df.to_excel('brand.xlsx')



# for i in pHref:
#     from selenium.webdriver.chrome.service import Service
#     from selenium import webdriver
#     from selenium.webdriver.common.action_chains import ActionChains
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.support.ui import WebDriverWait
#     from selenium.webdriver.support import expected_conditions as EC
#
#     s = Service(r"C:\Users\ilyx\Desktop\chromedriver.exe")
#     driver = webdriver.Chrome(service=s)
#
#     # URL страницы товара
#     url = i
#
#     # Открываем страницу товара
#     driver.get(url)
#
#
#
#     # Ожидание появления кнопки "Смотреть все отзывы" до 10 секунд
#     all_reviews_button = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '.wb-review-more')))
#
#     # эмулируем щелчок на кнопке "Смотреть все отзывы"
#     ActionChains(driver).move_to_element(all_reviews_button).click().perform()
#
#     # Получаем ссылку на страницу отзывов
#     reviews_link = driver.current_url
#
#     # Вывод ссылки на страницу отзывов
#     print('Ссылка на страницу отзывов:', reviews_link)
#
#     # Закрываем браузер
#     driver.quit()

