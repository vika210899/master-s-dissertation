from text_processing import TextProcessing
import pandas as pd
import xlsx_in_txt
import time
import spacy

st_txt = time.time()
st_txt_ns = time.time_ns()
test_text = xlsx_in_txt.read_data()
test_text = test_text[0:100]
fin_txt = time.time() - st_txt
fin_txt_ns = time.time_ns() - st_txt_ns


st_df = time.time()
nlp = spacy.load('ru_core_news_sm')

df = pd.DataFrame({#'Nlp_load': [TextProcessing().tok_only(sent, nlp)[0] for sent in test_text],
                    # 'Doc_load': [TextProcessing().tok_only(sent, nlp)[1] for sent in test_text],
                    'Tok_only': [TextProcessing().tok_only(sent, nlp) for sent in test_text],
                    'Tok_filter': [TextProcessing().tok_filter(sent, nlp) for sent in test_text],
                    'Tok_ents': [TextProcessing().tok_ents(sent, nlp) for sent in test_text],
                    'Tok_filter_ents': [TextProcessing().tok_filter_ents(sent, nlp) for sent in test_text],
                    'Tok_checkPOS': [TextProcessing().tok_checkPOS(sent, nlp) for sent in test_text],
                    'Tok_filter_checkPOS': [TextProcessing().tok_filter_checkPOS(sent, nlp) for sent in test_text] })
fin_df = time.time() - st_df
df.to_excel('result_tests/result_of_tests_4_t.xlsx', index=False)
