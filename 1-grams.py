# decomposition into 1-grams
import time
# from spacy.lang.ru import Russian
import textacy
import spacy

# start_SpaCy = time.time()
# print(time.time() - start_SpaCy, ' - SpaCy')

text = "Пушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого». Я-то из-за угла вышел 7 апреля."
# text = "London is the capital and most populous city of England and the United Kingdom.  Standing on the River Thames in the south east of the island of Great Britain, London has been a major settlement for two millennia. It was founded by the Romans, who named it Londinium."

# nlp = Russian()
# nlp = spacy.load('en_core_web_lg')
nlp = spacy.load('ru_core_news_sm')

# 0.	Исходный текст поступает на вход
doc = nlp(text)

# 1. Сегментация + 2. Токенизация + 4. Удаление стоп-слов + 4* Удаление цифр
ngrams = [ngram for n in range(1, 4)
          for ngram in textacy.extract.ngrams(doc, n)]  # , filter_stops=True, filter_nums=True)]
print(ngrams)

# result_SpaCy = list(textacy.extract.ngrams(doc, 1, filter_stops=True, filter_nums=True))
# print(result_SpaCy) 

# # 2*.	*Промежуточный необязательный шаг* – определение частей речи
# print("Часть речи: ")
# for token in doc:
#     token_text = token.text
#     token_pos = token.pos_
#     print(token_text, ' - ', token_pos)
# # либо 
# print({token.text: token.pos_ for token in doc})

# # 3.	Лемматизация: токены приводятся к начальной форме
# print("Лемматизация: ")
# for token in doc:
#     token_text = token.text
#     token_lemma = token.lemma_
#     print(token_text, ' - ', token_lemma)
# # либо
# print({token.text: token.lemma_ for token in doc})
# # либо
# print(' '.join([token.lemma_ for token in doc]))

# # 4.	Удаление стоп-слов (добавлено в п.1), слишком коротких слов
# # ----------------------------------

# # 4*.	*Промежуточный необязательный шаг* – удаление цифр (добавлено в п.1)

# # 4**.	*Промежуточный необязательный шаг* – парсинг зависимостей
# print("Зависимости от других слов: ")
# for token in doc:
#     token_text = token.text
#     token_head = token.head.text
#     print(token_text, ' - ', token_head)

# # 4**.	*Промежуточный необязательный шаг* – роль в предложении
# print("Роль в предложении: ")
# for token in doc:
#     token_text = token.text
#     token_dep = token.dep_
#     print(token_text, ' - ', token_dep)

# # + отрисовка зависимостей слов в предложении
# from spacy import displacy
# from pathlib import Path
# svg = displacy.render(doc, style="dep")
# output_path = Path("images/sentence.svg")
# output_path.open("w", encoding="utf-8").write(svg)

# 4***.	*Промежуточный необязательный шаг* – группы существительных
# ----------------------------------

# # 4****.	*Промежуточный необязательный шаг* – поиск именованных сущностей 
# распознаются и простые имена и фамилии!!!!!!!!!!!!!!
# for ent in doc.ents:
#     print(ent.text, ent.label_)
# # либо
# for entity in doc.ents:
#     print(f"{entity.text} ({entity.label_})")

# 4*****.	Можно еще внести распознавание семантической близости, но так как все кластеры будут похожи 
# ----------------------------------











# не работает для русского

# # Извлечение фрагментов
# noun_chunks = textacy.extract.noun_chunks(doc, min_freq=3)
# print([noun_chunk for noun_chunk in noun_chunks])
# # Перевод в нижний регистр
# noun_chunks = map(str, noun_chunks)
# noun_chunks = map(str.lower, noun_chunks)
# print(noun_chunks)

# # вывод всех фрагментов, состоящих из 2 слов и более
# for noun_chunk in set(noun_chunks):
#     if len(noun_chunk.split(" ")) > 1:
#         print(noun_chunk)





# for token in doc:
#     token_text = token.text
#     token_pos = token.pos_
#     token_dep = token.dep_
#     token_head = token.head.text
#     token_lemma = token.lemma_
#     print(f"{token_text:<16}{token_lemma:<16}{token_pos:<10}" \
#           f"{token_dep:<10}{token_head:<12}")

