from text_processing import TextProcessing

# тестовый текст
text = 'Виктория Терещенко говорит, что После отправке на печать МФУ не печатает, бумага есть тонер есть. ошибки не выдает бумага не зажевана, компьютер и МФУ были перезагружены.'
# text = 'Повышенный шум вентилятора в системном блоке'
print([word for word in TextProcessing().preprocess(text)])  # вывод токенов (из результата функции preprocess модуля text_processing)
