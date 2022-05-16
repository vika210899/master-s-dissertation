import textacy
from spacy import displacy
from pathlib import Path
import textacy.resources
import time
import spacy


# Определение частей речи
def get_pos(doc, result):
    pos_res = list(spacy.explain(token.pos_) for token in doc for token_ in result for x in token_ if token.text == x.text)
    return pos_res


# Лемматизация
def get_lemma(doc, result):
    lemm_res = list(spacy.explain(token.lemma_) for token in doc for token_ in result for x in token_ if token.text == x.text)
    return lemm_res


# Парсинг зависимостей
def get_relation(doc, result):
    relation_res = list(spacy.explain(token.head.text) for token in doc for token_ in result for x in token_ if token.text == x.text)
    return relation_res


# + Отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep")
    output_path = Path("images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


# Роль в предложении
def get_role(doc, result):
    role_res = list(spacy.explain(token.dep_) for token in doc for token_ in result for x in token_ if token.text == x.text)
    return role_res


# Поиск именованных сущностей
# распознаются и простые имена и фамилии!!!!!!!!!!!!!! д.б. написаны в определенном порядке
def get_ents(doc):
    ents_res = list(ent.label_ for ent in doc.ents)
    return ents_res


# Удаление именованных сущностей
def remove_ents(document, result_tokenize):
    for ent in document.ents:
        for n_gramm in result_tokenize:
            for x in n_gramm:
                if str(ent) == str(x):
                    result_tokenize.remove(n_gramm)
    return result_tokenize


# Поиск синонимов
def get_synonymss(token):
    rs = textacy.resources.ConceptNet()
    # rs.download()
    syn = rs.get_synonyms(term=token.lemma_, lang="ru", sense="n")
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
