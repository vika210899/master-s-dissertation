from text_processing import TextProcessing
import xlsx_in_txt
import spacy


test_text = xlsx_in_txt.read_data()
test_text = test_text[0] #16, 14

nlp = spacy.load('ru_core_news_sm')
n = 3

print('tok_only')
TextProcessing().tok_only(test_text, nlp, n)
print('\ntok_filter')
TextProcessing().tok_filter(test_text, nlp, n)
print('\ntok_ents')
TextProcessing().tok_ents(test_text, nlp, n)
print('\ntok_filter_ents')
TextProcessing().tok_filter_ents(test_text, nlp, n)
print('\ntok_checkPOS')
TextProcessing().tok_checkPOS(test_text, nlp, n)
print('\ntok_filter_checkPOS')
TextProcessing().tok_filter_checkPOS(test_text, nlp, n)
