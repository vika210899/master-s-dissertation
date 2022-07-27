from text_processing import TextProcessing
import xlsx_in_txt
import spacy


test_text = xlsx_in_txt.read_data()  # запускаем чтение данных из файла xlsx
# выбираем строку, которую хотим обработать (номера элементов списка с данными начинается с нуля)
test_text = test_text[0]  # 16, 14 - это те номера сообщений, над которыми экспериментировала я

nlp = spacy.load('ru_core_news_sm')  # загружаем языковую модель spacy
n = 3  # указываем тип элемента декомпозиции (1 - униграммы, 2 - биграммы, 3 - триграммы, 4 - смешанная декомпозиция)

# выводим результаты для каждого реализованного декомпозитора
print('tok_only')  # Токенизация без фильтрации
TextProcessing().tok_only(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
print('\ntok_filter')  # Токенизация с фильтрацией стоп-слов и цифр
TextProcessing().tok_filter(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
print('\ntok_ents')  # Токенизация с фильтрацией именных сущностей
TextProcessing().tok_ents(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
print('\ntok_filter_ents')  # Токенизация с фильтрацией стоп-слов, цифр и именных сущностей
TextProcessing().tok_filter_ents(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
print('\ntok_checkPOS')  # Токенизация без фильтрации и с отбором определенных частей речи
TextProcessing().tok_checkPOS(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
print('\ntok_filter_checkPOS')  # Токенизация с фильтрацией стоп-слов и цифр и отбором определенных частей речи
TextProcessing().tok_filter_checkPOS(test_text, nlp, n)  # вызываем необходимую функцию декомпозиции
