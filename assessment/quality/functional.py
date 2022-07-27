import textacy
import spacy
from spacy import displacy
from pathlib import Path
import textacy.resources
from config import Constants


# Определение частей речи 
# вывод расшифровки тега pos: print(spacy.explain(token.pos_) for token in result)
def get_pos(result, n):
    result_new = [] # список для записи результатов функции
    # для униграмм (для n = 1)
    if n == 1:
        # для каждой униграммы в результате токенизации выясняем ее часть речи
        for n_gramm in result:
            result_new.append(n_gramm.pos_) # и добавляем часть речи в список результатов функции
                                            # .pos_ - встроенная функция определения частей речи из библиотеки spacy
    # для остальных (для n = 2, 3 или 4)
    else:
        # для каждого n-грамма в результате токенизации
        for n_gramm in result:
            n_gramm_new = [] # список записи частей речи для словосочетания
            # для каждого слова в словосочетании выясняем часть речи
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].pos_) # и записываем в список для словосочетания
            result_new.append(n_gramm_new) # и потом этот список заносим в большой список результатов
    return result_new


# Лемматизация
def get_lemma(result, n):
    result_new = [] # список для записи результатов функции
    # для униграмм (для n = 1)
    if n == 1:
        # для каждой униграммы в результате токенизации выясняем ее лемму
        for n_gramm in result:
            result_new.append(n_gramm.lemma_) # и добавляем лемму в список результатов функции
                                            # .lemma_ - встроенная функция определения начальной формы слова из библиотеки spacy
    # для остальных (для n = 2, 3 или 4)
    else:
        # для каждого n-грамма в результате токенизации
        for n_gramm in result:
            n_gramm_new = [] # список записи лемм для одного словосочетания
            # для каждого слова в словосочетании выясняем лемму
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].lemma_) # и записываем ее в список для словосочетания
            result_new.append(n_gramm_new) # и потом этот список заносим в большой список результатов
    return result_new


# Парсинг зависимостей
def get_relation(result, n):
    result_new = [] # список для записи результатов функции
    if n == 1: # для униграмм (для n = 1)
        for n_gramm in result: # для каждой униграммы в результате токенизации выясняем для нее главное слово (слово, от которого она зависит)
            result_new.append(n_gramm.head.text) # и добавляем его в список результатов функции
                                                # .head - встроенная функция определения главного слова из библиотеки spacy
                                                # .text - встроенная функция определения текстовой формы объекта doc
    else: # для остальных (для n = 2, 3 или 4)
        for n_gramm in result: # для каждого n-грамма в результате токенизации
            n_gramm_new = [] # создаем список зависимостей для одного словосочетания
            # для каждого слова в словосочетании выясняем главное слово
            for i in range(len(n_gramm)):
                n_gramm_new.append(n_gramm[i].head.text) # и записываем его в список для словосочетания
            result_new.append(n_gramm_new) # и потом этот список заносим в большой список результатов
    return result_new


# + Отрисовка зависимостей слов в предложении
def display_roles(doc):
    svg = displacy.render(doc, style="dep") # отрисовываем зависимости
    output_path = Path("images/sentence.svg") # создаем файл по указанному адресу
    output_path.open("w", encoding="utf-8").write(svg) # заносим схему зависимостей в указанный файл


# Роль в предложении
def get_role(result, n):
    result_new = [] # список для записи результатов функции
    if n == 1: # для униграмм (для n = 1)
        for n_gramm in result: # для каждой униграммы в результате токенизации выясняем ее роль в предложении
            result_new.append(n_gramm.dep_) # заносим роль в список результатов функции
                                            # .dep_ - встроенная функция определения роли слова в предложении из библиотеки spacy
    else: # для остальных (для n = 2, 3 или 4)
        for n_gramm in result:  # для каждого n-грамма в результате токенизации
            n_gramm_new = [] # создаем список ролей для одного словосочетания
            for i in range(len(n_gramm)): # для каждого слова в словосочетании выясняем роль
                n_gramm_new.append(n_gramm[i].dep_) # записываем ее в список для словосочетания
            result_new.append(n_gramm_new) # и потом этот список заносим в большой список результатов
    return result_new


# Поиск именованных сущностей, зависит от порядка написания
# "имя фамилия" -> "[имя фамилия]" - как одна сущности, например, "Виктория Терещенко" -> [Виктория Терещенко]
# а не "фамилия имя" -> "[фамилия], [имя]" - как две сущности, например, "Терещенко Виктория" -> [Терещенко, Виктория]
def get_ents(doc):
    ents_res = list(ent for ent in doc.ents) # список, в который заносятся все найденные в исходном тексте именные сущности
    return ents_res


# Удаление именованных сущностей
def remove_ents(document, result_tokenize):
    for ent in document.ents: # для каждой именной сущности
        for y in ent: # и для каждого слова в имееной сущности (если это словосочетание)
            for n_gramm in result_tokenize: # для каждого n-грамма в списке токенизации
                for x in n_gramm: # и для каждого слова в n-грамме (если это словосочетание)
                    if str(y) == str(x): # сравниваются каждая часть именованной сущности с каждой частью n-грамма, ищутся одинаковые
                        result_tokenize.remove(n_gramm) # и удаляются
                                                        # таким образом текст очищается от именных сущностей
                        break
    return result_tokenize # и на выходе остается очищенный текст


# Поиск синонимов
def get_synonymss(result, n):
    rs = textacy.resources.ConceptNet()  # модуль textacy для поиска синонимов
    # rs.download() # один раз запустить, чтобы загрузилась БЗ, потом закомментировать обратно
    result_new = [] # список для записи результатов функции
    if n == 1: # для униграмм (для n = 1)
        for n_gramm in result: # для каждой униграммы в результате токенизации выясняем ее роль в предложении
            syn = rs.get_synonyms(term=n_gramm.lemma_, lang="ru", sense="n") # получаем синонимы к униграмму
            result_new.append(syn) # и записываем их в список результатов функции
    else: # для остальных (для n = 2, 3 или 4)
        for n_gramm in result: # для каждого n-грамма в результате токенизации
            n_gramm_new = [] # создаем список синонимов для каждого словосочетания
            for i in range(len(n_gramm)): # для каждого слова в n-грамме
                syn = rs.get_synonyms(
                    term=n_gramm[i].lemma_, lang="ru", sense="n") # ищем синонимы
                n_gramm_new.append(syn) # записываем их в список для словосочетания
            result_new.append(n_gramm_new) # и потом этот список заносим в большой список результатов
    return result_new


# Удаление специализированных стоп-слов из собственного списка
def remove_spec_stop_words(result_tokenize, n):
    stop_words_list = [] # список для записи результатов функции
    # открываем файл со специализированными стоп-словами
    with open(Constants.STOPLIST_FILE_NAME, "r") as f:
        for line in f: # читаем построчно (одна строка = одно стоп-слово)
            stop_words_list.extend(line.split()) # заносим прочитанные слова в список
    # для униграмм (для n = 1)
    if n == 1:
        for word in stop_words_list: # для каждого специализированного стоп-слова
            for n_gramm in result_tokenize: # для каждой униграммы в результате токенизации
                if str(word) == str(n_gramm): # ищем специализированное стоп-слово в тексте
                    result_tokenize.remove(n_gramm) # и удаляем его
    # для остальных (для n = 2, 3 или 4)
    else:
        for word in stop_words_list: # для каждого специализированного стоп-слова
            for n_gramm in result_tokenize: # для каждого n-грамма в результате токенизации
                for x in n_gramm: # для каждого слова в словосочетании 
                    if str(word) == str(x): # ищем специализированное стоп-слово в тексте
                        result_tokenize.remove(n_gramm) # и удаляем его
    return result_tokenize # и на выходе остается очищенный текст


# Все вместе
def print_all_together(doc, result_tok):
    # печатаем шапку таблицы
    print(f"{'text':<16}{'lemma':<16}{'part of speach':<18}{'role':<10}{'dependent':<12}")
    # 1. для каждого слова из объекта doc 
    for token in doc:  ### token - токен из объекта doc (то есть одно слово из исходного текста)
        token_text = token.text # 2. присваиваем переменной token_text значение текстового написания токена из объекта doc 
        # 3. для каждого n-грамма из списка декомпозиции
        for token_ in result_tok:  ### token_ - токен (= n-грамм = словосочетание или слово) из декомпозированного doc (то есть из списка n-грамм - result_tok)
            # 4. далее для каждого слова из n-грамма (из словосочетания)
            for x in token_:  ### x - одно слово из n-грамма (из словосочетания)
                # 5. сравниваем слово token с x
                # делаем это для того, чтобы можно было вытащить всю остальную информацию для построения таблицы ниже
                # так как элемент объекта doc (token) хранит эту информацию (они являются типами token или span), а элементы списка result_tok (token_) уже не хранят 
                # (так как в функции лемматизации создается новый список из лемм, которые уже являются типом str)
                
                # 6. если текстовое значение token и x совпадают, то ищем оставшиеся параметры для таблицы
                if token_text == x.text:
                    token_lemma = token.lemma_ # ищем лемму токена
                    token_pos = token.pos_ # ищем часть речи токена
                                        # здесь можно поставить вместо "token.pos_" - spacy.explain(token.pos_), чтобы части речи писались полным названием, а не аббревиатурой
                    token_dep = token.dep_ # ищем роль токена в предложении
                    token_head = token.head.text # ищем главное слово (слово, от которого токен зависит)
                    # печатаем содержимое таблицы
                    print(
                        f"{token_text:<16}{token_lemma:<16}{token_pos:<18}"
                        f"{token_dep:<10}{token_head:<12}"
                    )
