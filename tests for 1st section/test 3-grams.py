from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

import textacy
from spacy.lang.ru import Russian
import time
from nltk import trigrams
from nltk.util import ngrams
from nltk.tokenize import ToktokTokenizer
# тестовый текст для Pattern, Scikit-learn, TextBlob
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
# тестовый текст для NLTK
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'


# NLTK trigrams
start_trigrams = time.time()  # чек начала времени работы алгоритма NLTK bigrams
trigrm = list(trigrams(ToktokTokenizer().tokenize(text1)))  # запускаем алгоритм для поиска униграмм
result = [' '.join(trigrmmmm) for trigrmmmm in trigrm]  # приводим список к красивому виду для распечатки
# print(result)
# result
print(time.time() - start_trigrams, ' - NLTK Trigrams')  # выводим время работы алгоритма NLTK bigrams


# NLTK ngrams
start_ngrams = time.time()  # чек начала времени работы алгоритма NLTK ngrams
_1gram = ToktokTokenizer().tokenize(text1)  # запускаем алгоритм для поиска униграмм
_3gram = [' '.join(e) for e in ngrams(_1gram, 3)]  # формирование списка триграмм на основе униграмм
# print(_3gram)
# _3gram
print(time.time() - start_ngrams, ' - NLTK Ngrams')  # выводим время работы алгоритма NLTK ngrams


# SpaCy
nlp = Russian()  # загружаем модель для работы с русским языком
# создаем объект doc
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")
start_spacy2 = time.time()  # чек начала времени работы алгоритма SpaCy
ngrams = list(textacy.extract.ngrams(doc, 3))  # запуск работы токенизатора для униграмм
# print(ngrams)
print(time.time() - start_spacy2, ' - SpaCy')  # выводим время работы алгоритма SpaCy


# Pattern
from pattern.ru import ngrams
start_pattern = time.time()  # чек начала времени работы алгоритма Pattern
result = ngrams(text, n=3)  # запуск работы токенизатора для триграмм
# print(result)
print(time.time() - start_pattern, ' - Pattern')  # выводим время работы алгоритма Pattern


# Scikit-learn
start_scikitlearn = time.time()  # чек начала времени работы алгоритма Scikit-learn
c_vec = CountVectorizer(ngram_range=(3, 3))  # функция, поддерживающая выделение n-грамм, задаем ей тип токена - триграммы
ngrams = c_vec.fit_transform([text])  # нормализуем входящий текст
vocab = c_vec.vocabulary_  # формируем словарь, состоящий из токенов
result = [token for token in vocab]  # переводим его в вид списка
# print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')  # выводим время работы алгоритма Scikit-learn

# TextBlob
start_textblob = time.time()  # чек начала времени работы алгоритма TextBlob
n_grams = list(TextBlob(text).ngrams(3))  # формируем список триграмм с помощью алгоритма 
result = [' '.join(grams) for grams in n_grams]  # приводим список в красивый вид для его распечатки
# print(result)
print(time.time() - start_textblob, ' - TextBlob')  # выводим время работы алгоритма TextBlob
