import tok
import functional
import spacy


class TextProcessing:

    def preprocess(self, raw_text):
    
        nlp = spacy.load('ru_core_news_sm')
        doc = nlp(raw_text)
        n = 4
        result_tok = tok.tokenize_filter_ents(doc, n)
        result_tok = functional.get_lemma(result_tok, n) 
        result_tok = functional.remove_spec_stop_words(result_tok, n)
        # print(result_tok)
        return list(token for token in result_tok)