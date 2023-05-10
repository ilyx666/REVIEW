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


# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_colwidth', None)

date = []
name = []
rating = []
feedback = []
feedback_id = []
kolvo_ph = []
likee = []
tovarId = []

with open("rewiew_href.json", "r", encoding='utf-8') as file:
    rewH = json.load(file)

for a, t in rewH.items():
    with open(f"review_html2/{a}.html", encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    find_name = soup.find_all('button', class_='feedback__header')
    find_date = soup.find_all('span', class_='feedback__date')
    find_star = soup.find_all('span')
    feedback_text = soup.find_all('p', class_='feedback__text')
    imageFB = soup.find_all('img', class_='j-feedback-photo')
    fb_id = soup.find_all('div', class_='feedback__content')
    like = soup.find_all('span', class_='vote__count')
    TI = soup.find_all('a', class_='product-line__name')
    k = 0
    #
    # for i in find_name:
    #     if k >= 1:
    #         print(i.text)
    #     k += 1


    for i in find_date:
        if k % 2 == 0:
            p = i.get('content').replace('T', ' ').replace('Z', ' ')
            datee = p[8:10] + '-' + p[5:7] + '-' + p[0:4] + ' ' + p[11:20]
            date.append(datee)

        k += 1



    for i in find_name:
            name.append(i.text)
    d = 0
    for i in TI:
        k = (i.get('href').split('/')[4])

    for i in range(len(name)-len(rating)):
        tovarId.append(k)

    for i in find_star:
        try:
            if len(i.get('class')) == 3:
                if i.get('class')[0] == 'feedback__rating':
                    rating.append(i.get('class')[2][4])

        except TypeError as ex:
            pass



    for i in feedback_text:
        try:
            feedback.append(i.text)
        except UnicodeEncodeError as ex:
            pass





    for i in fb_id:
        feedback_id.append(i.get('id'))



    for i in imageFB:
        par = i.findParent('div').get('id')
        kolvo_ph.append(par)
    photo = Counter(kolvo_ph)




    listt = []
    for i in feedback_id:
        i = str(i)

    for i in feedback_id:
        for j, h in photo.items():
            if i == j:
                listt.append(h)
                photo.pop(j)
            else:
                listt.append(0)
            break
    for i in range(len(feedback_id)-len(listt)):
        listt.append(0)


    k = 0
    for i in like:
        if k % 2 == 0:
            likee.append(i.text)
        k += 1



    # tovarId.append(a)



    # for i in find_name:
    #     print(i.get('data-link'))



print(len(feedback_id))
print(len(tovarId))
print(len(date))
print(len(name))
print(len(rating))
print(len(feedback))
print(len(listt))
print(len(likee))




df = pd.DataFrame({'rewiew_ID' : feedback_id,
                   'article' : tovarId,
                    'Date' : date,
                    'Name' : name,
                   'Rating' : rating,
                   'Rewiew' : feedback,
                   'amount Photo' : listt,
                   'amount LIKE' : likee})
df.to_excel('rewiewDOP.xlsx')
print(df)