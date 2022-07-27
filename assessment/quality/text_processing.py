import tok
import functional

class TextProcessing:

    # Токенизация без фильтрации
    def tok_only(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_only(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов

    # Токенизация с фильтрацией стоп-слов и цифр
    def tok_filter(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_filter(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов

    # Токенизация с фильтрацией стоп-слов, цифр и именных сущностей
    def tok_filter_ents(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_filter_ents(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов

    # Токенизация с фильтрацией именных сущностей
    def tok_ents(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_ents(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов

    # Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
    def tok_filter_checkPOS(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_filter_checkPOS(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов

    # Токенизация без фильтрации и с отбором определенных частей речи
    def tok_checkPOS(self, raw_text, nlp, n):
        doc = nlp(raw_text)  # создаем объект doc из исходного текста
        result_tok = tok.tokenize_checkPOS(doc, n)  # вызываем декомпозитор
        print(result_tok)  # выводим результат декомпозиции
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем результат декомпозиции
        print(result_tok)  # выводим лемматизированный результат декомпозиции
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем из получившегося списка специализированные стоп слова
        print(result_tok)  # выводим итоговый список лемм токенов
