import textacy
from spacy import displacy
from pathlib import Path
from functools import partial
import textacy.resources
import time

# 1. Сегментация + 2. Токенизация + 4. Удаление стоп-слов + 4* Удаление цифр
def tokenize_and_clean(document, n):
    result_SpaCy = list(
        textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True, include_pos={"NOUN", "ADJ"})
    )
    print(result_SpaCy)
    return result_SpaCy

# Виды токенизации:
# ** по дефолту
# ** с выбором критериев
# * классическая полная на n-граммы
# * с удалением стоп слов
# * с удалением цифр
# * с отбором определенных частей речи

# ngramsss = list(textacy.extract.ngrams, n=2, include_pos={"NOUN", "ADJ"})
# print(ngramsss)


# 2*. определение частей речи
def get_pos(doc, result):
    # print("Часть речи: ")
    # for token in doc:
    #     for token_ in result:
    #         token_text = token.text
    #         if token_text == token_.text:
    #             token_pos = token.pos_
    #             print(token_text, " - ", token_pos)

# либо
    print({token.text: token.pos_ for token in doc for token_ in result for x in token_ if token.text == x.text})

# 3.	Лемматизация
def get_lemma(doc, result):
    # print("Лемматизация: ")
    # for token in doc:
    #     for token_ in result:
    #         token_text = token.text
    #         if token_text == token_.text:
    #             token_lemma = token.lemma_
    #             print(token_text, " - ", token_lemma)
    # либо
    print({token.text: token.lemma_ for token in doc for token_ in result for x in token_ if token.text == x.text})
    # # либо
    # print(' '.join([token.lemma_ for token in doc]))
    # for token in doc:
    #     for token_ in result:
    #         token_text = token.text
    #         for x in token_:
    #             if token_text == x.text:
    #                 token_lemma = token.lemma_
    #                 print(token_text, " - ", token_lemma)


# 4**. парсинг зависимостей
def get_relation(doc, result):
    print("Зависимости от других слов: ")
    # for token in doc:
    #     token_text = token.text
    #     token_head = token.head.text
    #     print(token_text, " - ", token_head)
    print({token.text: token.head.text for token in doc for token_ in result for x in token_ if token.text == x.text})

# + отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep")
    output_path = Path("images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


# 4**. роль в предложении
def get_role(doc, result):
    print("Роль в предложении: ")
    # for token in doc:
    #     token_text = token.text
    #     token_dep = token.dep_
    #     print(token_text, " - ", token_dep)
    print({token.text: token.dep_ for token in doc for token_ in result for x in token_ if token.text == x.text})


# 4***.	n-граммы с существительным
def nouns_ngrams(doc):
    terms = list(
        textacy.extract.terms(
            doc,
            ngs=partial(
                textacy.extract.ngrams,
                n=2,
                filter_stops=True,
                filter_nums=True,
                include_pos={"NOUN", "ADJ"},
            ),
        )
    )  # , ents=partial(textacy.extract.entities, include_types={"PER", "ORG", "GPE", "LOC"}))) #, dedupe=True))
    print(terms)
    return terms


# 4****. поиск именованных сущностей
# распознаются и простые имена и фамилии!!!!!!!!!!!!!! д.б. написаны в определенном порядке
def get_ents(doc):
    for ent in doc.ents:
        print(ent.text, ent.label_)
    # либо
    # for entity in doc.ents:
    #     print(f"{entity.text} ({entity.label_})")
    # либо
    # ent_Spacy = list(textacy.extract.entities(doc))
    # return(ent_Spacy)

# 4*****.	Поиск синонимов
def get_synonymss(doc):
    rs = textacy.resources.ConceptNet()
    # rs.download()
    syn = rs.get_synonyms(term=doc[15].lemma_, lang="ru", sense="n")
    print(syn)
    return syn


# все вместе
def all_together(doc, result_tok):
    for token in doc:
        for token_ in result_tok:
            token_text = token.text
            for x in token_:
                if token_text == x.text:
                    token_pos = token.pos_
                    token_dep = token.dep_
                    token_head = token.head.text
                    token_lemma = token.lemma_
                    print(
                        f"{token_text:<16}{token_lemma:<16}{token_pos:<10}"
                        f"{token_dep:<10}{token_head:<12}"
                    )
