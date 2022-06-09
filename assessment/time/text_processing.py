from numpy import row_stack
import tok
import functional
import spacy
import time


class TextProcessing:

    def tok_only(self, raw_text, nlp):
        # time_nlp = time.time()
        # nlp = spacy.load('ru_core_news_sm')
        # fin_time_nlp = time.time() - time_nlp

        time_start = time.time()
        # time_doc = time.time()
        doc = nlp(raw_text)
        # fin_time_doc = time.time() - time_doc

        n = 4
        result_tok = tok.tokenize_only(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)
        time_finish = time.time() - time_start
        return time_finish

    def tok_filter(self, raw_text, nlp):
        time_start = time.time()
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_filter(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)

        time_finish = time.time() - time_start
        return time_finish

    def tok_filter_ents(self, raw_text, nlp):
        time_start = time.time()
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_filter_ents(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)

        time_finish = time.time() - time_start
        return time_finish

    def tok_ents(self, raw_text, nlp):
        time_start = time.time()
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_ents(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)

        time_finish = time.time() - time_start
        return time_finish

    def tok_filter_checkPOS(self, raw_text, nlp):
        time_start = time.time()
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_filter_checkPOS(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)

        time_finish = time.time() - time_start
        return time_finish

    def tok_checkPOS(self, raw_text, nlp):
        time_start = time.time()
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_checkPOS(doc, n)
        # result_tok = functional.get_lemma(result_tok, n)
        # result_tok = functional.remove_spec_stop_words(result_tok, n)

        time_finish = time.time() - time_start
        return time_finish
