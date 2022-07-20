import textacy
from spacy import displacy
from pathlib import Path
import textacy.resources
from config import Constants


# Определение частей речи (spacy.explain(token.pos_))
def get_pos(result, n):
    result_new = []
    # для униграмм (для n = 1)
    if n == 1:
        # для каждой униграммы в результате токенизации выясняем его часть речи
        for n_gramm in result:
            result_new.append(n_gramm.pos_)
    # для остальных (для n = 2, 3 или 4)
    else:
        # для каждой униграммы в результате токенизации
        for n_gramm in result:
            n_gramm_new = []
            # для каждого слова n-грамма выясняем часть речи
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].pos_)
            result_new.append(n_gramm_new)
    return result_new


# Лемматизация
def get_lemma(result, n):
    result_new = []
    # для униграмм (для n = 1)
    if n == 1:
        # для каждой униграммы в результате токенизации выясняем его лемму
        for n_gramm in result:
            result_new.append(n_gramm.lemma_)
    # для остальных (для n = 2, 3 или 4)
    else:
        # для каждой униграммы в результате токенизации
        for n_gramm in result:
            n_gramm_new = []
            # для каждого слова n-грамма выясняем лемму
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].lemma_)
            result_new.append(n_gramm_new)
    return result_new


# Парсинг зависимостей
def get_relation(result, n):
    result_new = []
    # для униграмм (для n = 1)
    if n == 1:
        # для каждой униграммы в результате токенизации выясняем его главное слово (слово, от которого оно зависит)
        for n_gramm in result:
            result_new.append(n_gramm.head.text)
    # для остальных (для n = 2, 3 или 4)
    else:
        # для каждой униграммы в результате токенизации
        for n_gramm in result:
            n_gramm_new = []
            # для каждого слова n-грамма выясняем главное слово
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].head.text)
            result_new.append(n_gramm_new)
    return result_new


# + Отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep")
    output_path = Path("images/sentence.svg")
    output_path.open("w", encoding="utf-8").write(svg)


# Роль в предложении
def get_role(result, n):
    result_new = []
    if n == 1:
        for n_gramm in result:
            result_new.append(n_gramm.dep_)
    else:
        for n_gramm in result:
            n_gramm_new = []
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].dep_)
            result_new.append(n_gramm_new)
    return result_new


# Поиск именованных сущностей, зависит от порядка написания
# "имя фамилия" -> "[имя фамилия]" - как одна сущности, например, "Виктория Терещенко" -> [Виктория Терещенко]
# а не "фамилия имя" -> "[фамилия], [имя]" - как две сущности, например, "Терещенко Виктория" -> [Терещенко, Виктория]
def get_ents(doc):
    ents_res = list(ent for ent in doc.ents)
    return ents_res


# Удаление именованных сущностей
def remove_ents(document, result_tokenize):
    for ent in document.ents:
        for y in ent:
            for n_gramm in result_tokenize:
                for x in n_gramm:
                    if str(y) == str(x):
                        result_tokenize.remove(n_gramm)
                        break
    return result_tokenize


# Поиск синонимов
def get_synonymss(result, n):
    rs = textacy.resources.ConceptNet()
    # rs.download()
    result_new = []
    if n == 1:
        for n_gramm in result:
            syn = rs.get_synonyms(term=n_gramm.lemma_, lang="ru", sense="n")
            result_new.append(syn)
    else:
        for n_gramm in result:
            n_gramm_new = []
            for i in range(len(n_gramm)):
                syn = rs.get_synonyms(
                    term=n_gramm[i].lemma_, lang="ru", sense="n")
                n_gramm_new.append(syn)
            result_new.append(n_gramm_new)
    return result_new


# Удаление специализированных стоп-слов из собственного списка
def remove_spec_stop_words(result_tokenize, n):
    stop_words_list = []

    with open(Constants.STOPLIST_FILE_NAME, "r") as f:
        for line in f:
            stop_words_list.extend(line.split())

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
def print_all_together(doc, result_tok):
    print(f"{'text':<16}{'lemma':<16}{'part of speach':<18}{'role':<10}{'dependent':<12}")
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
                        f"{token_text:<16}{token_lemma:<16}{token_pos:<18}"
                        f"{token_dep:<10}{token_head:<12}"
                    )
