import time
from nltk import bigrams
from nltk.util import ngrams
from nltk.tokenize import ToktokTokenizer
text = 'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'
text1 = u'Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».'

# NLTK bigrams
start_bigrams = time.time()
bigrm = list(bigrams(ToktokTokenizer().tokenize(text1)))
result = [' '.join(bigrmmmm) for bigrmmmm in bigrm]
# print(result)
result
print(time.time() - start_bigrams, ' - NLTK Bigrams')


# # NLTK ngrams 
start_ngrams = time.time()
_1gram = ToktokTokenizer().tokenize(text1)
_2gram = [' '.join(e) for e in ngrams(_1gram, 2)]
# print(_2gram)
_2gram
print(time.time() - start_ngrams, ' - NLTK Ngrams')


# SpaCy
from spacy.lang.ru import Russian
import textacy
nlp = Russian()
doc = nlp("Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого».")  

#---1---
# start_spacy1 = time.time()
# for n in range(1, len(doc)):
#     m = n-1
#     # token = (doc[m], doc[n])
#     token = doc[m:n+1]
#     print(token.text)
# print(time.time() - start_spacy1, ' - SpaCy 1')

#---2---
start_spacy2 = time.time()
ngrams = list(textacy.extract.ngrams(doc, 2))
# print(ngrams)
print(time.time() - start_spacy2, ' - SpaCy')


# Pattern 
from pattern.ru import ngrams
start_pattern = time.time()
result = ngrams(text, n=2)
# print(result)
print(time.time() - start_pattern, ' - Pattern')


# Gensim
#--- хорошая штука, но работает только с англ---
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
#-----------------------------------------------


# Scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
start_scikitlearn = time.time()
c_vec = CountVectorizer(ngram_range=(2, 2)) #(ngram_range=(1, 3))
ngrams = c_vec.fit_transform([text])
vocab = c_vec.vocabulary_
result = [token for token in vocab]
# print(result)
print(time.time() - start_scikitlearn, ' - Scikit-learn')


# TextBlob 
from textblob import TextBlob
start_textblob = time.time()
n_grams = list(TextBlob(text).ngrams(2))
result = [' '.join(grams) for grams in n_grams]
# print(result)
print(time.time() - start_textblob, ' - TextBlob')
