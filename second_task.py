"""2. Каждое из слов «class», «function», «method» записать в байтовом типе
без преобразования в последовательность кодов (не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных."""


b_class = b'class'
b_function = b'function'
b_method = b'method'

b_words = [b_class, b_function, b_method]

for word in b_words:
    print('\nТип переменной:', type(word), '\nСодержимое переменной: ', word, '\nДлина переменной: ', len(word))