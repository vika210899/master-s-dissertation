import tok
import functional
import spacy


class TextProcessing:

    def preprocess(self, raw_text):

        nlp = spacy.load('ru_core_news_sm')  # загружаем языковую панель
        doc = nlp(raw_text)  # формируется объект doc из raw_text
        n = 4  # вводится тип элементов декомпозиции (1 - униграммы, 2 - биграммы, 3 - триграммы, 4 - смешанная декомпозиция)
        result_tok = tok.tokenize_filter_ents(doc, n)  # производится токенизация по выбранному токенизатору (сейчас это tokenize_filter_ents)
        # сюда вставлять методы из functional.py (если в токенизаторе чего-то не хватает)
        # потому что после лемматизации в result_tok будут лежать str, а не span и token, которые нужны spacy для выполнения многих функций
        result_tok = functional.get_lemma(result_tok, n)  # лемматизируем полученные токены
        result_tok = functional.remove_spec_stop_words(result_tok, n)  # удаляем специализированные стоп слова
        return result_tok
