"""3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле
YAML-формата. Для этого:

a. Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке
ASCII (например, €);

b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить стилизацию файла
с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;

c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными."""

import yaml
import json


YAML_FILE = 'file.yaml'
JSON_FILE = 'orders.json'


def reading_yaml(file):
    with open(file, encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def reading_json(file):
    with open(file, encoding='utf-8') as f:
        return json.load(f)


def write_yaml(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

    res = reading_yaml(file)
    print(res == data)


if __name__ == "__main__":
    MY_DICK = reading_json(JSON_FILE)
    print(MY_DICK)
    write_yaml(MY_DICK, YAML_FILE)
