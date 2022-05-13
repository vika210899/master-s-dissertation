import textacy
from spacy import displacy
from pathlib import Path
from functools import partial
import textacy.resources
import time
import spacy


# Определение частей речи
def get_pos(doc, result):
    print("Часть речи: ")
    print(
        {
            token.text: spacy.explain(token.pos_)
            for token in doc
            for token_ in result
            for x in token_
            if token.text == x.text
        }
    )


# Лемматизация
def get_lemma(doc, result):
    print("Лемматизация: ")
    print(
        {
            token.text: token.lemma_
            for token in doc
            for token_ in result
            for x in token_
            if token.text == x.text
        }
    )


# Парсинг зависимостей
def get_relation(doc, result):
    print("Зависимости от других слов: ")
    print(
        {
            token.text: token.head.text
            for token in doc
            for token_ in result
            for x in token_
            if token.text == x.text
        }
    )


# + Отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep")
    output_path = Path("images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


# Роль в предложении
def get_role(doc, result):
    print("Роль в предложении: ")
    print(
        {
            token.text: token.dep_
            for token in doc
            for token_ in result
            for x in token_
            if token.text == x.text
        }
    )


# Поиск именованных сущностей
# распознаются и простые имена и фамилии!!!!!!!!!!!!!! д.б. написаны в определенном порядке
def get_ents(doc):
    for ent in doc.ents:
        print(ent.text, ent.label_)


# Поиск синонимов
def get_synonymss(doc):
    rs = textacy.resources.ConceptNet()
    # rs.download()
    syn = rs.get_synonyms(term=doc[15].lemma_, lang="ru", sense="n")
    print(syn)
    return syn


# Все вместе
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
