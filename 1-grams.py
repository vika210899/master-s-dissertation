# decomposition into 1-grams
import time
import spacy
import functional

text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля."
nlp = spacy.load('ru_core_news_sm')
doc = nlp(text)

# time_start = time.time()

result_SpaCy = functional.tokenize_and_clean(doc, 1)
# functional.get_ents(doc)
# functional.get_lemma(doc, result_SpaCy)  
# functional.get_pos(doc, result_SpaCy)  
# functional.get_relation(doc, result_SpaCy)
# functional.get_role(doc, result_SpaCy)
# functional.display_roles(doc)
# functional.get_synonymss(doc)
# terms = functional.nouns_ngrams(doc)
# functional.all_together(doc, result_SpaCy)

# print(time.time() - time_start)