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
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'

# NLTK unigrams + bigrams + trigrams
start_nltk = time.time()
ngrams_nltk = []
ngrams_nltk.extend([token] for token in ToktokTokenizer().tokenize(text1))
ngrams_nltk.extend(bigrams(ToktokTokenizer().tokenize(text1)))
ngrams_nltk.extend(trigrams(ToktokTokenizer().tokenize(text1)))
result = [' '.join(token) for token in ngrams_nltk]
# print(result)
print(time.time() - start_nltk, ' - NLTK 1+2+3')


# NLTK ngrams
start1 = time.time()
n_grams_nltk = []
for n in range(1, 4):
    n_grams_nltk.extend(ngrams(ToktokTokenizer().tokenize(text1), n))
result = list(' '.join(grams) for grams in n_grams_nltk)
# print(result)
print(time.time() - start1, ' - NLTK Ngrams')


# NLTK everygrams
start_every = time.time()
result = [token for token in everygrams(
    ToktokTokenizer().tokenize(text1), 1, 3)]
# print(result)
print(time.time() - start_every, ' - NLTK Everygrams')


# SpaCy DONE
nlp = Russian()
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")
start_spacy2 = time.time()
ngrams = [ngram for n in range(1, 4)
          for ngram in textacy.extract.ngrams(doc, n)]  # , filter_stops=True, filter_nums=True)]
# print(ngrams)
print(time.time() - start_spacy2, ' - SpaCy')


# Pattern
start_pattern = time.time()
ngramsss = [ngram for n in range(1, 4) for ngram in ngrams(text, n)]
# print(ngramsss)
print(time.time() - start_pattern, ' - Pattern')


# Scikit-learn
start_scikitlearn = time.time()
c_vec = CountVectorizer(ngram_range=(1, 3))
ngrams = c_vec.fit_transform([text])
vocab = c_vec.vocabulary_
result = [token for token in vocab]
# print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')


# TextBlob
start_textblob = time.time()
n_grams = []
for num in range(1, 4):
    n_grams.extend(TextBlob(text).ngrams(num))
result = list(' '.join(grams) for grams in n_grams)
# print(result)
print(time.time() - start_textblob, ' - TextBlob')
