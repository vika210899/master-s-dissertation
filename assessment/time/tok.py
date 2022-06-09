import textacy
import textacy.resources
import functional

# Токенизация без фильтрации
def tokenize_only(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False)
        )
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов и цифр
def tokenize_filter(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=True, filter_nums=True)
        )
    return result_SpaCy


# Токенизация без фильтрации и с отбором определенных частей речи
def tokenize_checkPOS(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"},)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"})
        )
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
def tokenize_filter_checkPOS(document, n):
    if n == 4:
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
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=True, filter_nums=True)
        )
    result_SpaCy = functional.remove_ents(document, result_SpaCy)
    # print(result_SpaCy)
    return result_SpaCy


# Токенизация с фильтрацией именных сущностей
def tokenize_ents(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
                        for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False)]
    else:
        result_SpaCy = list(
            textacy.extract.ngrams(
                document, n, filter_stops=False, filter_nums=False)
        )
    result_SpaCy = functional.remove_ents(document, result_SpaCy)
    return result_SpaCy
