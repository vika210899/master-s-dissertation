from textblob import TextBlob
import rutokenizer
from tensorflow.keras.preprocessing.text import Tokenizer
import tensorflow as tf
from sklearn.feature_extraction.text import CountVectorizer
from gensim.utils import simple_preprocess
from spacy.lang.ru import Russian
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import ToktokTokenizer
from nltk.tokenize import SpaceTokenizer
from nltk.tokenize import WhitespaceTokenizer
from nltk.tokenize import RegexpTokenizer
import time
# тестовый текст для RegexpTokenizer, WhitespaceTokenizer, SpaceTokenizer, TweetTokenizer, NLTKWordTokenizer, Re, Pattern, Gensim, TextBlob
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван.'
# тестовый текст для ToktokTokenizer, Rutokenizer
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван.'
# тестовый текст для Scikit-learn, Keras
text33 = ["Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван."]


# RegexpTokenizer
start_RegexpTokenizer = time.time()  # чек начала времени работы алгоритма RegexpTokenizer
tokenizer = RegexpTokenizer('\w+-\w+|\w+|[^\s+]')  # подбор формулы для токенизатора
# tokenizer = RegexpTokenizer('\s+', gaps = True)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
# tokenizer = RegexpTokenizer('\w+')  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
result_RegexpTokenizer = tokenizer.tokenize(text)  # запуск токенизатора с тестовым текстом для униграмм
# print(result_RegexpTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
print(time.time() - start_RegexpTokenizer, ' - RegexpTokenizer')  # выводим время работы алгоритма RegexpTokenizer


# WhitespaceTokenizer
start_WhitespaceTokenizer = time.time()  # чек начала времени работы алгоритма WhitespaceTokenizer
result_WhitespaceTokenizer = WhitespaceTokenizer().tokenize(text)  # запуск работы токенизатора для униграмм
# print(result_WhitespaceTokenizer)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
print(time.time() - start_WhitespaceTokenizer, ' - WhitespaceTokenizer')  # выводим время работы алгоритма WhitespaceTokenizer


# SpaceTokenizer
start_SpaceTokenizer = time.time()  # чек начала времени работы алгоритма SpaceTokenizer
result_SpaceTokenizer = SpaceTokenizer().tokenize(text)  # запуск работы токенизатора для униграмм
# print(result_SpaceTokenizer)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
print(time.time() - start_SpaceTokenizer, ' - SpaceTokenizer')  # выводим время работы алгоритма SpaceTokenizer


# ToktokTokenizer
start_ToktokTokenizer = time.time()  # чек начала времени работы алгоритма ToktokTokenizer
result_ToktokTokenizer = ToktokTokenizer().tokenize(text1)  # запуск работы токенизатора для униграмм
# print(result_ToktokTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
print(time.time() - start_ToktokTokenizer, ' - ToktokTokenizer')  # выводим время работы алгоритма ToktokTokenizer


# TweetTokenizer
start_TweetTokenizer = time.time()  # чек начала времени работы алгоритма TweetTokenizer
result_TweetTokenizer = TweetTokenizer().tokenize(text)  # запуск работы токенизатора для униграмм
# print(result_TweetTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
print(time.time() - start_TweetTokenizer, ' - TweetTokenizer')  # выводим время работы алгоритма TweetTokenizer


# NLTKWordTokenizer
start_NLTKWordTokenizer = time.time()  # чек начала времени работы алгоритма NLTKWordTokenizer
result_NLTKWordTokenizer = word_tokenize(text)  # запуск работы токенизатора  для униграмм
# print(result_NLTKWordTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
print(time.time() - start_NLTKWordTokenizer, ' - NLTKWordTokenizer')  # выводим время работы алгоритма NLTKWordTokenizer


# Re
start_Re = time.time()  # чек начала времени работы алгоритма Re
# подбор формулы
# result = re.findall(r'[^\W\d_]+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# result2 = re.findall(r'\w+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# result3 = re.findall(r'[А-Яа-яёЁ]+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# result4 = re.findall(r'\w+-\w+|\w+', text)  # ['Не', 'ветер', 'а', 'какой-то', 'ураган']
# print('Re 1: ', result)
result_Re = re.findall(r'\w+-\w+|\w+|[^\s+]', text)  # запуск работы токенизатора для униграмм
# print(result_Re)
# print(time.time() - start_Re, ' - Re')  # выводим время работы алгоритма Re


# SpaCy - токенизацию можно настроить
import textacy
nlp = Russian()  # загружаем модель для работы с русским языком
# создаем объект doc
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел.")
start_SpaCy = time.time()  # чек начала времени работы алгоритма SpaCy

result_SpaCy = list(textacy.extract.ngrams(doc, 1, filter_stops=False))  # запуск работы токенизатора для униграмм
# print(result_SpaCy)
print(time.time() - start_SpaCy, ' - SpaCy')  # выводим время работы алгоритма SpaCy


# Pattern
from pattern.ru import ngrams
start_pattern = time.time()  # чек начала времени работы алгоритма Pattern
result = ngrams(text, n=1)  # запуск работы токенизатора для униграмм
# print(result)
print(time.time() - start_pattern, ' - Pattern')  # выводим время работы алгоритма Pattern


# Gensim (может й приравнивать к и -- deacc = True)
start_Gensim = time.time()  # чек начала времени работы алгоритма Gensim
# print(simple_preprocess(text, deacc = True))  # ['не', 'ветер', 'какои', 'то', 'ураган']
result_Gensim = simple_preprocess(text)  # запуск работы токенизатора для униграмм
# print(result_Gensim)  # ['не', 'ветер', 'какой', 'то', 'ураган']
print(time.time() - start_Gensim, ' - Gensim')  # выводим время работы алгоритма Gensim


# Scikit-learn
start_Scikitlearn = time.time()  # чек начала времени работы алгоритма Scikit-learn
vectorizer = CountVectorizer()    # функция, поддерживающая выделение n-грамм (по умолчания - униграммы)
data = vectorizer.fit_transform(text33).toarray()  # создаем массив (матрицу) с нормализованным текстом для тестового текстового документа
vocab = vectorizer.get_feature_names_out()  # выделяем униграммы

result_Scikitlearn = []  # создание списка для записи униграмм
for word in vocab:
    result_Scikitlearn.extend(word.split())  # заносим каждый токен в итоговый список
# print(result_Scikitlearn)  # ['ветер', 'какой', 'не', 'то', 'ураган']
print(time.time() - start_Scikitlearn, ' - Scikit-learn')  # выводим время работы алгоритма Scikit-learn


# Keras
start_Keras = time.time()  # чек начала времени работы алгоритма Keras
tokenizer = Tokenizer(num_words=100)  # в переменную заносим значение токенизатора, который работает для первых 100 символов текста
tokenizer.fit_on_texts(text33)  # запускаем токенизатор для разметки нашего тестового текста
result_Keras = tokenizer.word_index  # запускаем токенизатор для униграмм
# print(result_Keras)  # {'не': 1, 'ветер': 2, 'а': 3, 'какой': 4, 'то': 5, 'ураган': 6}
print(time.time() - start_Keras, ' - Keras')  # выводим время работы алгоритма Keras


# Rutokenizer
start_Rutokenizer = time.time()  # чек начала времени работы алгоритма Rutokenizer
tokenizerr = rutokenizer.Tokenizer()  # в переменную заносим значение токенизатора для работы с русскими текстами
tokenizerr.load()  # загружаем его
result_Rutokenizer = [t for t in tokenizerr.tokenize(text1)]  # запуск работы токенизатора для униграмм
# print(result_Rutokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
print(time.time() - start_Rutokenizer, ' - Rutokenizer')  # выводим время работы алгоритма Rutokenizer


# TextBlob
start_TextBlob = time.time()  # чек начала времени работы алгоритма TextBlob
text_blob_object = TextBlob(text)  # в переменную заносим значение токенизатора для работы нашим текстом
document_sentence = text_blob_object.sentences  # проводим токенизацию на предложения
result_TextBlob = text_blob_object.words  # а теперь на униграммы
# print(result_TextBlob)  # ['Не', 'ветер', 'а', 'какой-то', 'ураган']
print(time.time() - start_TextBlob, ' - TextBlob')  # выводим время работы алгоритма TextBlob
