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




nameS = []
brandN = []
pID = []
pHref = []
with open(r"C:\Users\ilyx\Desktop\source-page.html", encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
name = soup.find_all('span', class_='product-card__name')
brand = soup.find_all('span', class_='product-card__brand')
product_id = soup.find_all('article')
hreff = soup.find_all('a', class_='product-card__link j-card-link j-open-full-product-card')

for i in hreff:
    pHref.append(i.get('href'))


for i in name:
    nameS.append(i.text.removeprefix(' / '))
for i in brand:
    brandN.append(i.text)
for i in product_id:
    pID.append(i.get('id').removeprefix('c'))
k = 0

# for i in nameS:
#     if i[0] != 'Н':
#         if i[0] != 'M':
#             brandN.pop(k)
#             nameS.pop(k)
#             pID.pop(k)
#             pHref.pop(k)
#     k += 1



print(len(nameS))
print(len(brandN))
print(len(pID))
print(len(pHref))

df = pd.DataFrame({'name': nameS,
                   'brand': brandN,
                    'id': pID,
                   'href': pHref})
print(df)
df2 = pd.read_excel(r'C:\Users\ilyx\Desktop\REVIEW-main\product.xlsx')

dfI = pd.concat([df2, df])
df.to_excel(r'C:\Users\ilyx\Desktop\product222.xlsx', index=False)
dfI.to_excel(r'C:\Users\ilyx\Desktop\product.xlsx', index=False)

