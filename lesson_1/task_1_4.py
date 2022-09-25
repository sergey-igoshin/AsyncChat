"""Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode)."""

WORDS_LIST = ['разработка', 'администрирование', 'protocol', 'standard']


def print_words(words):
    for i in words:
        i_encode = i.encode()
        print(f'{type(i_encode)} {i_encode}')

        i_decode = i_encode.decode('utf-8')
        print(f'{type(i_decode)} {i_decode}')


print_words(WORDS_LIST)
