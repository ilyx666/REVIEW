# coding=utf8
import re
import string
import nltk
from nltk.corpus import stopwords
from pymystem3 import Mystem
import emoji

# загружаем стоп-слова для русского языка
nltk.download('stopwords')
stop_words = set(stopwords.words('russian'))

# создаем объект лемматизатора
m = Mystem()

# функция для предобработки текста
def preprocess_text(text):
    # удаляем ссылки и хэштеги
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'#\S+', '', text)
    # удаляем знаки препинания
    text = text.translate(str.maketrans('', '', string.punctuation))
    # приводим к нижнему регистру
    text = text.lower()
    # лемматизируем текст
    lemmas = m.lemmatize(text)
    # удаляем стоп-слова
    filtered_lemmas = [lemma for lemma in lemmas if lemma.strip() and lemma not in stop_words]
    # объединяем леммы в строку
    filtered_text = ' '.join(filtered_lemmas)
    converted_review = emoji.demojize(filtered_text)
    return converted_review
