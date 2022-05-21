import time
import spacy
import functional
import tok

text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля в Минске в Газпроме."
nlp = spacy.load('ru_core_news_sm')
doc = nlp(text)

# time_start = time.time()
n = 1
result_SpaCy = tok.tokenize_only(doc, n)
# functional.get_ents(doc)
# functional.display_roles(doc)
# functional.get_synonymss(doc[15])

# functional.get_lemma(doc, result_SpaCy)  
functional.get_pos(doc, result_SpaCy, n)  
# functional.get_relation(doc, result_SpaCy)  
# functional.get_role(doc, result_SpaCy)  
# functional.all_together(doc, result_SpaCy)  

# functional.nouns_ngrams(doc)

# tok.tokenize_filter_ents(doc, 3)
# tok.tokenize_filter(doc, 3)
# tok.tokenize_only(doc, 3)
# tok.tokenize_checkPOS(doc, 3)
# tok.tokenize_filter_checkPOS(doc, 3)

# print(time.time() - time_start)
