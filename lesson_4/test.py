""" Для всех функций из урока 3 написать тесты с использованием unittest. Они должны быть оформлены в отдельных скриптах
с префиксом test_ в имени файла (например, test_client.py).
"""

from lesson_3.client import main as mc, get_response
from lesson_3.server import main as ms, get_action
from datetime import datetime
from unittest import TestCase


class TestClient(TestCase):
    HOST = 'localhost'
    PORT = 7777
    TIME = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    MESSAGE = 'None'
    ACTION = {'action': 'presence'}
    DATA = {
        'response': 200,
        'data': {
            'message': MESSAGE,
            'time': TIME
        }
    }

    def test_main_server(self):
        self.assertEqual(ms(self.HOST, self.PORT), 'Соединение не установлено')

    def test_main_client(self):
        self.assertEqual(mc(self.HOST, self.PORT), 'Соединение не установлено')

    def test_get_data(self):
        self.assertEqual(get_response(self.DATA), f'{self.MESSAGE} {self.TIME}')

    def test_get_action(self):
        self.assertEqual(get_action(self.ACTION), self.DATA)
