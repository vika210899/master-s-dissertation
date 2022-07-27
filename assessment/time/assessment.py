from text_processing import TextProcessing
import pandas as pd
import xlsx_in_txt
import time
import spacy

st_txt = time.time()  # фиксируем начало чтения данных из xlsx в секундах
st_txt_ns = time.time_ns()  # фиксируем начало чтения данных из xlsx в наносекундах
test_text = xlsx_in_txt.read_data()  # запускаем чтение данных из файла xlsx
test_text = test_text[500:600]  # выбираем диапазон строк, которые хотим обработать (номера элементов списка с данными начинается с нуля)
fin_txt = time.time() - st_txt  # фиксируем конец чтения данных из xlsx в секундах
fin_txt_ns = time.time_ns() - st_txt_ns  # фиксируем конец чтения данных из xlsx в наносекундах


st_df = time.time()  # фиксируем начало построения датафрейма в секундах
nlp = spacy.load('ru_core_news_sm')  # загружаем модель spacy для русского языка
# формируем датафрейм [одна строка кода ниже = один столбец формируемой таблицы]
df = pd.DataFrame({  # 'Nlp_load': [TextProcessing().tok_only(sent, nlp)[0] for sent in test_text],  # здесь время загрузки модели spacy для русского языка
    # 'Doc_load': [TextProcessing().tok_only(sent, nlp)[1] for sent in test_text],  # время формирования объекта doc
    'Tok_only': [TextProcessing().tok_only(sent, nlp) for sent in test_text],  # время работы токенизатора Tok_only
    'Tok_filter': [TextProcessing().tok_filter(sent, nlp) for sent in test_text],  # время работы токенизатора Tok_filter
    'Tok_ents': [TextProcessing().tok_ents(sent, nlp) for sent in test_text],  # время работы токенизатора Tok_ents
    'Tok_filter_ents': [TextProcessing().tok_filter_ents(sent, nlp) for sent in test_text],  # время работы токенизатора Tok_filter_ents
    'Tok_checkPOS': [TextProcessing().tok_checkPOS(sent, nlp) for sent in test_text],  # время работы токенизатора Tok_checkPOS
    'Tok_filter_checkPOS': [TextProcessing().tok_filter_checkPOS(sent, nlp) for sent in test_text]})  # время работы токенизатора Tok_filter_checkPOS
fin_df = time.time() - st_df  # фиксируем конец построения датафрейма в секундах
df.to_excel('result_tests/result_of_tests_4_t.xlsx', index=False)  # записываем датафрейм в эксель
