from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

import textacy
from spacy.lang.ru import Russian
import time
from nltk import trigrams
from nltk.util import ngrams
from nltk.tokenize import ToktokTokenizer
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'


# NLTK trigrams
start_trigrams = time.time()
trigrm = list(trigrams(ToktokTokenizer().tokenize(text1)))
result = [' '.join(trigrmmmm) for trigrmmmm in trigrm]
print(result)
# result
print(time.time() - start_trigrams, ' - NLTK Trigrams')


# NLTK ngrams
start_ngrams = time.time()
_1gram = ToktokTokenizer().tokenize(text1)
_3gram = [' '.join(e) for e in ngrams(_1gram, 3)]
print(_3gram)
# _3gram
print(time.time() - start_ngrams, ' - NLTK Ngrams')


# SpaCy
nlp = Russian()
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")
# ---1---
# start_spacy = time.time()
# for n in range(1, len(doc)):
#     m = n-1
#     # token = (doc[m], doc[n])
#     token = doc[m:n+2]
#     print(token.text)
# print(time.time() - start_spacy, ' - SpaCy')

# ---2---
start_spacy2 = time.time()
ngrams = list(textacy.extract.ngrams(doc, 3))
print(ngrams)
print(time.time() - start_spacy2, ' - SpaCy')


# Pattern
from pattern.ru import ngrams
start_pattern = time.time()
result = ngrams(text, n=3)
print(result)
print(time.time() - start_pattern, ' - Pattern')


# Scikit-learn
start_scikitlearn = time.time()
c_vec = CountVectorizer(ngram_range=(3, 3))
ngrams = c_vec.fit_transform([text])
vocab = c_vec.vocabulary_
result = [token for token in vocab]
print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')

# TextBlob
start_textblob = time.time()
n_grams = list(TextBlob(text).ngrams(3))
result = [' '.join(grams) for grams in n_grams]
print(result)
print(time.time() - start_textblob, ' - TextBlob')
