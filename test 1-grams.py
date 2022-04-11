import time
text = 'Я - к.т.н., живу в США.' 
# 'Не ветер, а какой-то ураган!'
# 'Я-то из-за угла вышел.'
# 'Я - к.т.н., живу в США.'
# 'В Нью-Йорке (США) хорошие маффины стоят $3.88.' 


# RegexpTokenizer
start_time1 = time.time()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer('\w+-\w+|\w+|[^\s+]')  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# tokenizer = RegexpTokenizer('\s+', gaps = True)  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']
# tokenizer = RegexpTokenizer('\w+')  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
print(tokenizer.tokenize(text), ', ', time.time() - start_time1, ' - RegexpTokenizer')


# WhitespaceTokenizer
start_time2 = time.time()
from nltk.tokenize import WhitespaceTokenizer
print(WhitespaceTokenizer().tokenize(text), ', ', time.time() - start_time2, ' - WhitespaceTokenizer')  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']


# SpaceTokenizer
start_time3 = time.time()
from nltk.tokenize import SpaceTokenizer
print(SpaceTokenizer().tokenize(text), ', ', time.time() - start_time3, ' - SpaceTokenizer')  # ['Не', 'ветер,', 'а', 'какой-то', 'ураган!']


# ToktokTokenizer
start_time4 = time.time()
from nltk.tokenize import ToktokTokenizer
text1 = u'Я - к.т.н., живу в США.'
print(ToktokTokenizer().tokenize(text1), ', ', time.time() - start_time4, ' - ToktokTokenizer')  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']


# TweetTokenizer
start_time5 = time.time()
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
print(TweetTokenizer().tokenize(text), ', ', time.time() - start_time5, ' - TweetTokenizer')  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']


# NLTKWordTokenizer
start_time6 = time.time()
from nltk.tokenize import word_tokenize
print(word_tokenize(text), ', ', time.time() - start_time6, ' - NLTKWordTokenizer')  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']


# Re
start_time8 = time.time()
import re
result = re.findall(r'[^\W\d_]+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
result2 = re.findall(r'\w+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
result3 = re.findall(r'[А-Яа-яёЁ]+', text)  # ['Не', 'ветер', 'а', 'какой', 'то', 'ураган']
result4 = re.findall(r'\w+-\w+|\w+', text)  # ['Не', 'ветер', 'а', 'какой-то', 'ураган']
result5 = re.findall(r'\w+-\w+|\w+|[^\s+]', text)  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']
# print('Re 1: ', result)
print(result5, ', ', time.time() - start_time8, ' - Re')


# SpaCy - токенизацию можно настроить
start_time9 = time.time()
from spacy.lang.ru import Russian
nlp = Russian()
doc = nlp("Я - к.т.н., живу в США.") 
print([token.text for token in doc], ', ', time.time() - start_time9, ' - SpaCy')  # ['Не', 'ветер', ',', 'а', 'какой', '-', 'то', 'ураган', '!']


# Pattern
# start_time10 = time.time()
# from pattern.text.en import parse
# from pprint import pprint
# pprint(parse('I drove my car to the hospital yesterday', relations=True, lemmata=True))
# print(parse('I drove my car to the hospital yesterday', relations=True, lemmata=True).split())


# Gensim (может й приравнивать к и -- deacc = True)
start_time11 = time.time()
from gensim.utils import simple_preprocess
# print(simple_preprocess(text, deacc = True))  # ['не', 'ветер', 'какои', 'то', 'ураган']
print(simple_preprocess(text), ', ', time.time() - start_time11, ' - Gensim')  # ['не', 'ветер', 'какой', 'то', 'ураган']


# Scikit-learn
start_time12 = time.time()
from sklearn.feature_extraction.text import CountVectorizer
text33 = ["Я - к.т.н., живу в США."] 
vectorizer = CountVectorizer()
data = vectorizer.fit_transform(text33).toarray()
vocab = vectorizer.get_feature_names_out()

required_list = []
for word in vocab:
    required_list.extend(word.split())
print(required_list, ', ', time.time() - start_time12, ' - Scikit-learn')  # ['ветер', 'какой', 'не', 'то', 'ураган']


# Keras
start_time13 = time.time()
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
textA = ["Я - к.т.н., живу в США."] 
tokenizer = Tokenizer(num_words=100)
tokenizer.fit_on_texts(textA)
word_indexes = tokenizer.word_index
print(word_indexes, ', ', time.time() - start_time13, ' - Keras')  # {'не': 1, 'ветер': 2, 'а': 3, 'какой': 4, 'то': 5, 'ураган': 6}


# Rutokenizer
start_time14 = time.time()
import rutokenizer
t = rutokenizer.Tokenizer()
t.load()
print([t for t in t.tokenize(u'Я - к.т.н., живу в США.')], ', ', time.time() - start_time14, ' - Rutokenizer')  # ['Не', 'ветер', ',', 'а', 'какой-то', 'ураган', '!']


# TextBlob
start_time15 = time.time()
from textblob import TextBlob
text_blob_object = TextBlob(text)
document_sentence = text_blob_object.sentences
document_words = text_blob_object.words
print(document_words, ', ', time.time() - start_time15, ' - TextBlob')  # ['Не', 'ветер', 'а', 'какой-то', 'ураган']


