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

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_excel(r'C:\Users\ilyx\Desktop\product.xlsx')
review_dict = {}
op = 0
for i in df.id:
    with open(fr"C:\Users\ilyx\Desktop\html\{i}.html", encoding='utf-8') as file:
        src = file.read()
# with open(r"C:\Users\ilyx\Desktop\html\135608212.html", encoding='utf-8') as file:
#     src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    rew = soup.find_all('span', class_='product-review__count-review')
    review_href = soup.find('a', class_='comment-card__hide-link j-feedback-text j-read-full-feedback')
    article = soup.find('p', class_='product-article')

    kolvoRew = []
    k = 0
    try:
        for j in rew:
            kolvoRew.append(j.text[1:].split(' ')[0])
            k = int(j.text[1:].split(' ')[0])
        a = article.text.split(' ')[3]
        if k > 3:
            review_dict[int(a)] = 'https://www.wildberries.ru' + review_href.get('href')
        else:
            pass
        print(i)
    except Exception as ex:
        pass
    print(len(review_dict))
with open(r"C:\Users\ilyx\Desktop\rewiew_href.json", "w", encoding="utf-8") as file:
    json.dump(review_dict, file)


