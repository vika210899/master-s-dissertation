import tok
import functional
import time


class TextProcessing:

    def tok_only(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)

        result_tok = tok.tokenize_only(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n) 
        print(result_tok)
        time_finish = time.time() - time_start
        return time_finish


    def tok_filter(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)
        result_tok = tok.tokenize_filter(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n)
        print(result_tok)     

        time_finish = time.time() - time_start
        return time_finish
    

    def tok_filter_ents(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)
        result_tok = tok.tokenize_filter_ents(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n)
        print(result_tok)     

        time_finish = time.time() - time_start
        return time_finish
    

    def tok_ents(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)
        result_tok = tok.tokenize_ents(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n)
        print(result_tok)     

        time_finish = time.time() - time_start
        return time_finish


    def tok_filter_checkPOS(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)
        result_tok = tok.tokenize_filter_checkPOS(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n)   
        print(result_tok)  

        time_finish = time.time() - time_start
        return time_finish

    
    def tok_checkPOS(self, raw_text, nlp, n):
        time_start = time.time()
        doc = nlp(raw_text)
        result_tok = tok.tokenize_checkPOS(doc, n)
        print(result_tok)
        result_tok = functional.get_lemma(result_tok, n) 
        print(result_tok)
        result_tok = functional.remove_spec_stop_words(result_tok, n)
        print(result_tok)     

        time_finish = time.time() - time_start
        return time_finish