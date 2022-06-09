import spacy
import functional
import tok

text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля в Минске в Газпроме."
nlp = spacy.load('ru_core_news_sm')
doc = nlp(text)

n = 2
result_SpaCy = tok.tokenize_only(doc, n)
# print(functional.get_ents(doc))
# functional.display_roles(doc)
# print(functional.get_synonymss(result_SpaCy, n))
# print(functional.get_lemma(result_SpaCy, n))
# print(functional.get_pos(result_SpaCy, n))
# print(functional.get_relation(result_SpaCy, n))
# print(functional.get_role(result_SpaCy, n))
# print(functional.print_all_together(doc, result_SpaCy))
# print(functional.remove_ents(doc, result_SpaCy))

# print(tok.tokenize_filter_ents(doc, n))
# print(tok.tokenize_filter(doc, n))
# print(tok.tokenize_only(doc, n))
# print(tok.tokenize_checkPOS(doc, n))
# print(tok.tokenize_filter_checkPOS(doc, n))
# print(tok.tokenize_ents(doc, n))
