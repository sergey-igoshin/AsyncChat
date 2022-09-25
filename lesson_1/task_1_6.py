"""Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import locale


def write_file(file, lines):
    with open(file, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def print_file(file, encoding):
    with open(file, 'r', encoding=encoding) as f:
        print(f.read())


LINES = ['сетевое программирование', 'сокет', 'декоратор']
FILE = 'test_file.txt'
ENCODING = ['utf-8', 'cp1251']

print(f'Кодировка по умолчанию: {locale.getpreferredencoding()}', '\n')

write_file(FILE, LINES)
for i in ENCODING:
    print(f'Кодировка: {i}')
    try:
        print_file(FILE, i)
    except UnicodeDecodeError as e:
        print(e)
    finally:
        print()
