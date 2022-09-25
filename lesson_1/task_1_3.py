"""Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе."""

WORDS_LIST = [b'attribute', 'класс'.encode(), 'функция'.encode(), b'type']


def print_words(words):
    for i in words:
        print(f'{type(i)} {i}')


print_words(WORDS_LIST)
# «класс», «функция» невозможно записать в байтовом типе без encode().
