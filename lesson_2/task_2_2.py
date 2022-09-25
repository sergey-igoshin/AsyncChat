"""2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах. Написать
скрипт, автоматизирующий его заполнение данными. Для этого:

a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
orders.json. При записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json
from datetime import datetime
from random import choice

ITEM = ['LENOVO', 'ACER', 'DELL']
QUANTITY = [1, 2, 3]
PRICE = [100000.00, 145000.00, 58000.00]
BAYER = ['Ivanov', 'Petrov', 'Sidorov']
DATETIME = datetime.now()
CURRENCY = ['€', '$']


def write_order_to_json(**kwargs):
    with open('orders.json', encoding='utf-8') as f:
        data = json.load(f)
        data['orders'].append(kwargs)

    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    for _ in range(3):
        write_order_to_json(
            item=choice(ITEM),
            quantity=choice(QUANTITY),
            price=choice(PRICE),
            buyer=choice(BAYER),
            date=DATETIME.strftime("%d-%m-%Y %H:%M"),
            currency=choice(CURRENCY)
        )
