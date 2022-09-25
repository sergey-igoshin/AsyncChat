"""Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных."""

WORDS_BYTES_LIST = [b'class', b'function', b'method']


def print_words(words):
    for i in words:
        print(f'{type(i)} {i} {len(i)}')


print_words(WORDS_BYTES_LIST)
