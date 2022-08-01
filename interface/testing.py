# файл тестирования (можно удалить)
import spacy
import functional
import tok

# Введение тестового фрагмента текста
text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля в Минске в Газпроме."
nlp = spacy.load('ru_core_news_sm')  # загрузка модели spacy для обработки русского языка
doc = nlp(text)  # создание объекта doc

n = 2  # тип элемента декомпозиции (здесь - биграммы)
result_SpaCy = tok.tokenize_only(doc, n)  # активация выбранного декомпозитора

# проверка каждого метода из functional.py
# print(functional.get_ents(doc))
# functional.display_roles(doc)
# print(functional.get_synonymss(result_SpaCy, n))
# print(functional.get_lemma(result_SpaCy, n))
# print(functional.get_pos(result_SpaCy, n))
# print(functional.get_relation(result_SpaCy, n))
# print(functional.get_role(result_SpaCy, n))
# print(functional.print_all_together(doc, result_SpaCy))
# print(functional.remove_ents(doc, result_SpaCy))

# проверка каждого токенизатора из tok.py
# print(tok.tokenize_filter_ents(doc, n))
# print(tok.tokenize_filter(doc, n))
# print(tok.tokenize_only(doc, n))
# print(tok.tokenize_checkPOS(doc, n))
# print(tok.tokenize_filter_checkPOS(doc, n))
# print(tok.tokenize_ents(doc, n))
