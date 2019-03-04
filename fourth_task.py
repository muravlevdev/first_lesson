"""4. Преобразовать слова «разработка», «администрирование», «protocol»,
 «standard» из строкового представления в байтовое и выполнить обратное
 преобразование (используя методы encode и decode)."""

str_development = 'разработка'
str_administration = 'администрирование'
str_protocol = 'протокол'
str_standard = 'standard'

str_words = [str_development, str_administration, str_protocol, str_standard]

for word in str_words:
    b_word = word.encode()
    print( '\nСлово в байтовом представлении: ', b_word, '\nСлово в строковом представлении: ', b_word.decode())