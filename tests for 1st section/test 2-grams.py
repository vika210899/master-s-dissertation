from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
import textacy
from spacy.lang.ru import Russian
import time
from nltk import bigrams
from nltk.util import ngrams
from nltk.tokenize import ToktokTokenizer
# тестовый текст для Pattern, Scikit-learn, TextBlob
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
# тестовый текст для NLTK
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'

# NLTK bigrams
start_bigrams = time.time()  # чек начала времени работы алгоритма NLTK bigrams
bigrm = list(bigrams(ToktokTokenizer().tokenize(text1)))  # запускаем алгоритм для поиска биграмм
result = [' '.join(bigrmmmm) for bigrmmmm in bigrm]  # приводим список к красивому виду для распечатки
# print(result)
# result
print(time.time() - start_bigrams, ' - NLTK Bigrams')  # выводим время работы алгоритма NLTK bigrams


# NLTK ngrams
start_ngrams = time.time()  # чек начала времени работы алгоритма NLTK ngrams
_1gram = ToktokTokenizer().tokenize(text1)  # запускаем алгоритм для поиска униграмм
_2gram = [' '.join(e) for e in ngrams(_1gram, 2)]  # формирование списка биграмм на основе униграмм
# print(_2gram)
# _2gram
print(time.time() - start_ngrams, ' - NLTK Ngrams')  # выводим время работы алгоритма NLTK ngrams


# SpaCy
nlp = Russian()  # загружаем модель для работы с русским языком
# создаем объект doc
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")
start_spacy = time.time()  # чек начала времени работы алгоритма SpaCy
ngrams = list(textacy.extract.ngrams(doc, 2))  # запуск работы токенизатора для поиска биграмм
# print(ngrams)
print(time.time() - start_spacy, ' - SpaCy')  # выводим время работы алгоритма SpaCy


# Pattern
from pattern.ru import ngrams
start_pattern = time.time()  # чек начала времени работы алгоритма Pattern
result = ngrams(text, n=2)  # запуск работы токенизатора для биграмм
# print(result)
print(time.time() - start_pattern, ' - Pattern')  # выводим время работы алгоритма Pattern


# Gensim
# --- хорошая штука, но работает только с англ ---
# from gensim.models import Phrases
# from gensim.models.phrases import Phraser
# documents = ["the mayor of new york was there", "machine learning can be useful sometimes","new york mayor was present"]
# sentence_stream = [doc.split(" ") for doc in documents]
# print(sentence_stream)

# bigram = Phrases(sentence_stream, min_count=1, threshold=3, delimiter=' ')
# bigram_phraser = Phraser(bigram)
# print(bigram_phraser)

# for sent in sentence_stream:
#     tokens_ = bigram_phraser[sent]
#     print(tokens_)
# -----------------------------------------------


# Scikit-learn
start_scikitlearn = time.time()  # чек начала времени работы алгоритма Scikit-learn
c_vec = CountVectorizer(ngram_range=(2, 2))  # функция, поддерживающая выделение n-грамм, задаем ей тип токена - биграммы
ngrams = c_vec.fit_transform([text])  # нормализуем входящий текст
vocab = c_vec.vocabulary_  # формируем словарь, состоящий из токенов
result = [token for token in vocab]  # переводим его в вид списка
# print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')  # выводим время работы алгоритма Scikit-learn


# TextBlob
start_textblob = time.time()  # чек начала времени работы алгоритма TextBlob
n_grams = list(TextBlob(text).ngrams(2))  # формируем список биграмм с помощью алгоритма 
result = [' '.join(grams) for grams in n_grams]  # приводим список в красивый вид для его распечатки
# print(result)
print(time.time() - start_textblob, ' - TextBlob')  # выводим время работы алгоритма TextBlob
