"""3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

str_attribute = 'attribute'
str_class = 'класс'
str_function = 'функция'
str_type = 'type'
a = 'dd'
words = [str_attribute, str_class, str_function, str_type]

for word in words:
    try:
        b_word = word.encode('ascii')
    except Exception:
        print('Ошибка, слово "', word, '" нельзя привести в байтовый вид кодировки ascii')
    else:
        if b_word.decode('ascii') == word:
            print('Слово "', word, '" может быть приведено в байтовый вид кодировки ascii')
        else:
            print('Ошибка при проверке корректности преобразования слова %a' % (word))