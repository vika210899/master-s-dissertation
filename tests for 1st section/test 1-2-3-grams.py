from nltk import trigrams
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from pattern.ru import ngrams
import textacy
from spacy.lang.ru import Russian
from nltk.util import everygrams
from nltk.util import ngrams
from nltk import bigrams
from nltk.tokenize import ToktokTokenizer
import time

# вводим тестовый текст для Pattern, Scikit-learn, TextBlob
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
# вводим тестовый текст для NLTK
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'

# NLTK unigrams + bigrams + trigrams
start_nltk = time.time()  # чек начала времени работы алгоритма NLTK 1+2+3
ngrams_nltk = []  # создание списка для записи n-граммов
ngrams_nltk.extend([token] for token in ToktokTokenizer().tokenize(text1))  # добавялем в список униграммы
ngrams_nltk.extend(bigrams(ToktokTokenizer().tokenize(text1)))  # добавялем в список биграммы
ngrams_nltk.extend(trigrams(ToktokTokenizer().tokenize(text1)))  # добавялем в список триграммы
result = [' '.join(token) for token in ngrams_nltk]  # возвращаем список, состоящий из униграмм, биграмм и триграмм
# print(result)
print(time.time() - start_nltk, ' - NLTK 1+2+3')  # выводим время работы алгоритма NLTK 1+2+3


# NLTK ngrams
start1 = time.time()  # чек начала времени работы алгоритма NLTK Ngrams
n_grams_nltk = []  # создание списка для записи n-граммов
for n in range(1, 4):
    n_grams_nltk.extend(ngrams(ToktokTokenizer().tokenize(text1), n))  # формируем список n-грамм для n=1,2,3
result = list(' '.join(grams) for grams in n_grams_nltk)  # сохраняем список в красивом для распечатки виде
# print(result)
print(time.time() - start1, ' - NLTK Ngrams')  # выводим время работы алгоритма NLTK Ngrams


# NLTK everygrams
start_every = time.time()  # чек начала времени работы алгоритма NLTK Everygrams
result = [token for token in everygrams(
    ToktokTokenizer().tokenize(text1), 1, 3)]  # формируем список n-гргамм (для n=1,2,3)  
# print(result)
print(time.time() - start_every, ' - NLTK Everygrams')  # выводим время работы алгоритма NLTK Everygrams


# SpaCy DONE
nlp = Russian()  # загружаем модель для работы с русским языком
# создаем объект doc
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")
start_spacy2 = time.time()  # чек начала времени работы алгоритма SpaCy 
ngrams = [ngram for n in range(1, 4)
          for ngram in textacy.extract.ngrams(doc, n)]  # , filter_stops=True, filter_nums=True)]  # формируем список n-гргамм (для n=1,2,3) 
# print(ngrams)
print(time.time() - start_spacy2, ' - SpaCy')  # выводим время работы алгоритма SpaCy


# Pattern
start_pattern = time.time()  # чек начала времени работы алгоритма Pattern
ngramsss = [ngram for n in range(1, 4) for ngram in ngrams(text, n)]  # формируем список n-гргамм (для n=1,2,3) 
# print(ngramsss)
print(time.time() - start_pattern, ' - Pattern')  # выводим время работы алгоритма Pattern


# Scikit-learn
start_scikitlearn = time.time()  # чек начала времени работы алгоритма Scikit-learn 
c_vec = CountVectorizer(ngram_range=(1, 3))  # функция, поддерживающая выделение n-грамм, задаем ей тип токена (от униграмм до триграмм)
ngrams = c_vec.fit_transform([text])  # нормализуем входящий текст
vocab = c_vec.vocabulary_  # формируем словарь, состоящий из токенов и их матричных номеров 
result = [token for token in vocab]  # переводим его в вид списка
# print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')  # выводим время работы алгоритма Scikit-learn


# TextBlob
start_textblob = time.time()  # чек начала времени работы алгоритма TextBlob
n_grams = []  # создание списка для записи n-граммов
for num in range(1, 4):
    n_grams.extend(TextBlob(text).ngrams(num))  # формируем список n-гргамм (для n=1,2,3) 
result = list(' '.join(grams) for grams in n_grams)  # сохраняем список в красивом для распечатки виде
# print(result)
print(time.time() - start_textblob, ' - TextBlob')  # выводим время работы алгоритма TextBlob
