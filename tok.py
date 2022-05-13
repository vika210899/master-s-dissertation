import textacy
import textacy.resources
import time

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
    print(result_SpaCy)
    return result_SpaCy


# по умолчанию
# Токенизация с фильтрацией стоп-слов и цифр
def tokenize_filter(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
               for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        result_SpaCy = list(
        textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)
        )
    print(result_SpaCy)
    return result_SpaCy


# Токенизация без фильтрации и с отбором определенных частей речи
def tokenize_checkPOS(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
               for ngram in textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"},)]
    else:
        result_SpaCy = list(
        textacy.extract.ngrams(document, n, filter_stops=False, filter_nums=False, include_pos={"NOUN", "ADJ"})
        )
    print(result_SpaCy)
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
def tokenize_filter_checkPOS(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
               for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True, include_pos={"NOUN", "ADJ"})]
    else:
        result_SpaCy = list(
        textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True, include_pos={"NOUN", "ADJ"})
        )
    print(result_SpaCy)
    return result_SpaCy


# Токенизация с фильтрацией стоп-слов, цифр и именных сущностей
def tokenize_filter_ents(document, n):
    if n == 4:
        result_SpaCy = [ngram for n in range(1, 4)
               for ngram in textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)]
    else:
        result_SpaCy = list(
        textacy.extract.ngrams(document, n, filter_stops=True, filter_nums=True)
        )
    result_SpaCy = remove_ents(document, result_SpaCy)
    print(result_SpaCy)
    return result_SpaCy


# Поиск именованных сущностей
def remove_ents(document, result_tokenize):
    for ent in document.ents:
        for n_gramm in result_tokenize:
            for x in n_gramm:
                if str(ent) == str(x):
                    result_tokenize.remove(n_gramm)
    return result_tokenize
