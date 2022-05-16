import textacy
from spacy import displacy
from pathlib import Path
from functools import partial
import textacy.resources
import time
import spacy
from config import Constants


# Определение частей речи (spacy.explain(token.pos_))
def get_pos(result):
    result_new = []
    for n_gramm in result:
        result_new.append(n_gramm.pos_)
    return result_new


# Лемматизация
def get_lemma(result, n):
    result_new = []
    if n == 1:
        for n_gramm in result:
            result_new.append(n_gramm.lemma_)
    else:
        for n_gramm in result:
            n_gramm_new = []
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].lemma_)
            result_new.append(n_gramm_new)
    return result_new


# Парсинг зависимостей
def get_relation(result):
    result_new = []
    for n_gramm in result:
        result_new.append(n_gramm.head.text)
    return result_new


# + Отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep")
    output_path = Path("images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


# Роль в предложении
def get_role(result):
    result_new = []
    for n_gramm in result:
        result_new.append(n_gramm.dep_)
    return result_new


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


# Удаление специализированных стоп-слов из собственного списка
def remove_spec_stop_words(result_tokenize, n):
        stop_words_list = []

        with open(Constants.STOPLIST_FILE_NAME, "r") as f:
            for line in f:
                stop_words_list.extend(line.split()) 
        
        print(stop_words_list)
        if n == 1:
            for word in stop_words_list:
                for n_gramm in result_tokenize:
                    if str(word) == str(n_gramm):
                        result_tokenize.remove(n_gramm)
        else:
            for word in stop_words_list:
                for n_gramm in result_tokenize:
                    for x in n_gramm:
                        if str(word) == str(x):
                            result_tokenize.remove(n_gramm)
        return result_tokenize


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
