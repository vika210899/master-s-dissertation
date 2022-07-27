import textacy
import textacy.resources
import functional


# Токенизация без фильтрации
def tokenize_only(document, n):  # здесь document - это объект doc, сформированный в 11 строке text_processing.py; n - тип элемента декомпозиции
    # если смешанная декомпозиция, то проводим процедуру декомпозиции для каждого типа токена
    if n == 4: 
        # для каждого n от 1 до 4 
        # каждый n-грамм (или токен) из document добавляется в список result_SpaCy 
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False)]  # filter_stops=False - стоп-слова не удаляются (если True - слоп-слова будут удалены)
                                                                                                                  # filter_nums=False - цифры, числа не удаляются (если True - цифры, числа будут удалены)
        # в данном случае не удаляется ничего (фильтрация отключена)
    # если n = 1, 2 или 3, то проводим декомпозицию для конкретного типа токена
    else:
        # здесь также формируется список токенов заданного типа из document
        # и также отсутствует фильтрация
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False)
        )
    # на выходе получаем сформированный список токенов нужного типа
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов и цифр
def tokenize_filter(document, n):
    if n == 4:
        # здесь вместе с декомпозицией отслеживаются (автоматически, с помощью подключенных библиотек) стоп-слова и цифры/числа и удаляются
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        # здесь вместе с декомпозицией отслеживаются (автоматически, с помощью подключенных библиотек) стоп-слова и цифры/числа и удаляются
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=True, filter_nums=True)
        )
    return result_SpaCy


# Токенизация без фильтрации и с отбором определенных частей речи
def tokenize_checkPOS(document, n):
    if n == 4:
        # здесь не фильтруются стоп-слова и цифры/числа
        # но вместе с декомпозицией выделяются (автоматически, с помощью подключенных библиотек) только существительные (NOUN) и прилагательные (ADJ)
        # можно выбирать другие части речи
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"})]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"})
        )
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
def tokenize_filter_checkPOS(document, n):
    if n == 4:
        # здесь фильтруются стоп-слова и цифры/числа
        # и выделяются (автоматически, с помощью подключенных библиотек) только существительные (NOUN) и прилагательные (ADJ)
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True, include_pos={"NOUN", "ADJ"})]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=True, filter_nums=True, include_pos={"NOUN", "ADJ"})
        )
    return result_SpaCy


# по умолчанию
# Токенизация с фильтрацией стоп-слов, цифр и именных сущностей
def tokenize_filter_ents(document, n):
    # здесь сразу происходит декомпозиция с фильтрацией стоп-слов и цифр/чисел
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=True, filter_nums=True)
        )
    # а потом из result_SpaCy удаляются именные сущности
    result_SpaCy = functional.remove_ents(document, result_SpaCy)
    return result_SpaCy


# Токенизация с фильтрацией именных сущностей
def tokenize_ents(document, n):
    # здесь сразу происходит декомпозиция без фильтрации
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False)
        )
    # а потом из result_SpaCy удаляются именные сущности
    result_SpaCy = functional.remove_ents(document, result_SpaCy)
    return result_SpaCy
