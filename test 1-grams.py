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
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван.'
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван.'
text33 = ["Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». А кровать-то не диван."]
# 'Не ветер, а какой-то ураган!'
# 'Я-то из-за угла вышел.'
# 'Я - к.т.н., живу в США.'
# 'В Нью-Йорке (США) хорошие маффины стоят $3.88.'


# # RegexpTokenizer
# start_RegexpTokenizer = time.time()
# tokenizer = RegexpTokenizer('\w+-\w+|\w+|[^\s+]')
# # tokenizer = RegexpTokenizer('\s+', gaps = True)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
# # tokenizer = RegexpTokenizer('\w+')  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# result_RegexpTokenizer = tokenizer.tokenize(text)
# # print(result_RegexpTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print(time.time() - start_RegexpTokenizer, ' - RegexpTokenizer')


# # WhitespaceTokenizer
# start_WhitespaceTokenizer = time.time()
# result_WhitespaceTokenizer = WhitespaceTokenizer().tokenize(text)
# # print(result_WhitespaceTokenizer)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
# print(time.time() - start_WhitespaceTokenizer, ' - WhitespaceTokenizer')


# # SpaceTokenizer
# start_SpaceTokenizer = time.time()
# result_SpaceTokenizer = SpaceTokenizer().tokenize(text)
# # print(result_SpaceTokenizer)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
# print(time.time() - start_SpaceTokenizer, ' - SpaceTokenizer')


# # ToktokTokenizer
# start_ToktokTokenizer = time.time()
# result_ToktokTokenizer = ToktokTokenizer().tokenize(text1)
# # print(result_ToktokTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print(time.time() - start_ToktokTokenizer, ' - ToktokTokenizer')  


# # TweetTokenizer
# start_TweetTokenizer = time.time()
# result_TweetTokenizer = TweetTokenizer().tokenize(text)
# # print(result_TweetTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print(time.time() - start_TweetTokenizer, ' - TweetTokenizer')  


# # NLTKWordTokenizer
# start_NLTKWordTokenizer = time.time()
# result_NLTKWordTokenizer = word_tokenize(text)
# # print(result_NLTKWordTokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print(time.time() - start_NLTKWordTokenizer, ' - NLTKWordTokenizer')


# # Re
# start_Re = time.time()
# # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# # result = re.findall(r'[^\W\d_]+', text)
# # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# # result2 = re.findall(r'\w+', text)
# # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
# # result3 = re.findall(r'[А-Яа-яёЁ]+', text)
# # ['Не', 'ветер', 'а', 'какой-то', 'ураган']
# # result4 = re.findall(r'\w+-\w+|\w+', text)
# # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# # print('Re 1: ', result)
# result_Re = re.findall(r'\w+-\w+|\w+|[^\s+]', text)
# # print(result_Re)
# # print(time.time() - start_Re, ' - Re')


# SpaCy - токенизацию можно настроить
import textacy
nlp = Russian()
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел.")
start_SpaCy = time.time()

result_SpaCy = list(textacy.extract.ngrams(doc, 1, filter_stops=False))
print(result_SpaCy)
print(time.time() - start_SpaCy, ' - SpaCy')


# # Pattern
# from pattern.ru import ngrams
# start_pattern = time.time()
# result = ngrams(text, n=1)
# # print(result)
# print(time.time() - start_pattern, ' - Pattern')


# # Gensim (может й приравнивать к и -- deacc = True)
# start_Gensim = time.time()
# # print(simple_preprocess(text, deacc = True))  # ['не', 'ветер', 'какои', 'то', 'ураган']
# result_Gensim = simple_preprocess(text)
# # print(result_Gensim)  # ['не', 'ветер', 'какой', 'то', 'ураган']
# print(time.time() - start_Gensim, ' - Gensim')  


# # Scikit-learn
# start_Scikitlearn = time.time()
# vectorizer = CountVectorizer()
# data = vectorizer.fit_transform(text33).toarray()
# vocab = vectorizer.get_feature_names_out()

# result_Scikitlearn = []
# for word in vocab:
#     result_Scikitlearn.extend(word.split())
# # print(result_Scikitlearn)  # ['ветер', 'какой', 'не', 'то', 'ураган']
# print(time.time() - start_Scikitlearn, ' - Scikit-learn')


# # Keras
# start_Keras = time.time()
# tokenizer = Tokenizer(num_words=100)
# tokenizer.fit_on_texts(text33)
# result_Keras = tokenizer.word_index
# print(result_Keras)  # {'не': 1, 'ветер': 2, 'а': 3, 'какой': 4, 'то': 5, 'ураган': 6}
# print(time.time() - start_Keras, ' - Keras')


# # Rutokenizer
# start_Rutokenizer = time.time()
# tokenizerr = rutokenizer.Tokenizer()
# tokenizerr.load()
# result_Rutokenizer = [t for t in tokenizerr.tokenize(text1)]
# # print(result_Rutokenizer)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print(time.time() - start_Rutokenizer, ' - Rutokenizer')  


# # TextBlob
# start_TextBlob = time.time()
# text_blob_object = TextBlob(text)
# document_sentence = text_blob_object.sentences
# result_TextBlob = text_blob_object.words
# # print(result_TextBlob)  # ['Не', 'ветер', 'а', 'какой-то', 'ураган']
# print(time.time() - start_TextBlob, ' - TextBlob')
