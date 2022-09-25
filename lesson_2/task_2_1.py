"""1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в
него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;

c. Проверить работу программы через вызов функции write_to_csv().
"""

import re
import csv

FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
CSV_FILE = 'test.csv'
HEADER = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
RE = [
    HEADER[0] + r':\s+([a-zA-Z]+)',
    HEADER[1] + r':\s+([a-zA-Z0-9А-Яа-я\s\.]{1,})[\n]',
    HEADER[2] + r':\s+([-0-9a-zA-Z]+)',
    HEADER[3] + r':\s+([-0-9a-zA-Z\s]+)[\n]'
]


def re_get_content(file):
    with open(file, encoding='cp1251') as f:
        res = f.read()
        return (','.join(re.findall(i, res)) for i in RE)


def get_data():
    main_data = [HEADER]
    for file in FILES:
        os_prod_list, os_name_list, os_code_list, os_type_list = re_get_content(file)
        main_data.append([os_prod_list, os_name_list, os_code_list, os_type_list])
    return main_data


def write_to_csv(file):
    with open(file, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, delimiter=',', lineterminator="\r")
        data = get_data()
        for i in data:
            write_csv.writerow(i)


if __name__ == "__main__":
    write_to_csv(CSV_FILE)
