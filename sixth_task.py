"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку файла
по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое."""

# 1. Запись строк в файл

file_text = 'сетевое программирование\nсокет\nдекоратор'

with open('test_file.txt', 'w') as file:
    file.write(file_text)

# 2. Проверка кодировки файла

# PyCharm подсказал, что файл по умолчанию генерится в windows-1251, поэтому я добавил её в список проверяемых
# кодировок
encodings = ['windows-1251', 'ascii', 'utf-8']

# Код ниже не выполняется, так как даже с верной кодировкой b_text немного не совпадает с text_checker
# Что делаю не так, понять не смог

with open('test_file.txt', 'rb') as file:
    b_text = file.read()
    for encoding in encodings:
        try:
            text_checker = file_text.encode(encoding)
            if b_text == text_checker:
                print("Верная кодировка", encoding)
            else:
                print('Кодировка не является искомой: ', encoding)
        except Exception:
            print('Кодировка не является искомой: ', encoding)


# 3. Принудительное открытие

# Так как файл по умолчанию создаётся в кодировке windows-1251, то принудительно открыть его в юникоде не вышлло

with open('test_file.txt', 'r+', encoding='windows-1251') as file:
    print(file.read())
