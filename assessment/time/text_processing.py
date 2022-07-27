from numpy import row_stack
import tok
import functional
import spacy
import time

# время работы токенизаторов считается с процессом построения объекта doc, потому что иначе многие значения времени были бы 0.0 (даже в микросекундах),
# что не было наглядными значениями для исследования. То есть в действительности время работы еще меньше,
# чем в исследованиях у меня в дипломной работе 
class TextProcessing:

    # Токенизация без фильтрации
    def tok_only(self, raw_text, nlp):
        # time_nlp = time.time()  # фиксируем время начала загрузки модели ru_core_news_sm
        # nlp = spacy.load('ru_core_news_sm')  # загружаем модель
        # fin_time_nlp = time.time() - time_nlp  # фиксируем время конца загрузки
        
        # считаем время выполнения токенизации
        time_start = time.time()  # запоминаем время начала декомпозиции
        # time_doc = time.time()  # запоминаем время начала формирования объекта doc
        doc = nlp(raw_text)  # создаем doc
        # fin_time_doc = time.time() - time_doc  # запоминаем время конца формирования doc и считаем продолжительность процедуры формирования doc

        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_only(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова
        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора

    # Токенизация с фильтрацией стоп-слов и цифр
    def tok_filter(self, raw_text, nlp):
        time_start = time.time()  # запоминаем время начала декомпозиции
        doc = nlp(raw_text)  # создаем объект doc
        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_filter(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова

        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора

    # Токенизация с фильтрацией стоп-слов, цифр и именных сущностей
    def tok_filter_ents(self, raw_text, nlp):
        time_start = time.time()  # запоминаем время начала декомпозиции
        doc = nlp(raw_text)  # создаем объект doc
        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_filter_ents(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова

        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора

    # Токенизация с фильтрацией именных сущностей
    def tok_ents(self, raw_text, nlp):
        time_start = time.time()  # запоминаем время начала декомпозиции
        doc = nlp(raw_text)  # создаем объект doc
        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_ents(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова

        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора

    # Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
    def tok_filter_checkPOS(self, raw_text, nlp):
        time_start = time.time()  # запоминаем время начала декомпозиции
        doc = nlp(raw_text)  # создаем объект doc
        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_filter_checkPOS(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова

        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора

    # Токенизация без фильтрации и с отбором определенных частей речи
    def tok_checkPOS(self, raw_text, nlp):
        time_start = time.time()  # запоминаем время начала декомпозиции
        doc = nlp(raw_text)  # создаем объект doc
        n = 4  # задаем тип элемента декомпозиции
        result_tok = tok.tokenize_checkPOS(doc, n)  # запускаем декомпозицию исхдного текста и записываем результат в result_tok
        # result_tok = functional.get_lemma(result_tok, n)  # лемматизируем список токенов
        # result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова

        time_finish = time.time() - time_start  # фиксируем время завершения процессов декомпозиции
        return time_finish  # возвращаем время работы декомпозитора
