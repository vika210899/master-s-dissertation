from text_processing import TextProcessing

text = 'После отправке на печать МФУ не печатает, бумага есть тонер есть. ошибки не выдает бумага не зажевана, компьютер и МФУ были перезагружены.'

print([word for word in TextProcessing().preprocess(text)])