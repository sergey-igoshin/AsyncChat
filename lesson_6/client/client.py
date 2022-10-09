import socket
import json
import argparse
from client_log_config import logger
import inspect


def log(func):
    def call(*args, **kwargs):
        logger.info(f'Функция {func.__name__}() вызвана из функции {inspect.stack()[1][3]}')
        res = func(*args, **kwargs)
        logger.info(f'{func.__name__}() вернула {res}')
        return res
    return call


@log
def parse_client_arguments():
    parser = argparse.ArgumentParser(description="Клиент")
    parser.add_argument('-a', '--addr', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)
    args = parser.parse_args()
    return args.addr, args.port


@log
def message_dumps(**kwargs):
    return json.dumps(kwargs)


@log
def get_response(data):
    if data.get('response') == 200:
        return f"{data.get('address')} {data.get('data')['message']} {data.get('data')['time']}"
    return data.get('error')


def main():
    host, port = parse_client_arguments()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            clientsocket.connect((host, port))

            logger.debug('Соединение с сервером установлено')

            while True:
                message = input('> ')
                MSG = message_dumps(
                    action='presence',
                    message=message,
                )
                clientsocket.send(MSG.encode())
                data = clientsocket.recv(1024)

                response = json.loads(data.decode('utf-8'))
                get_data_response = get_response(response)

                print(get_data_response)
                logger.debug(get_data_response)
    except KeyboardInterrupt:
        logger.critical('Соединение с сервером разорвано')
    except ConnectionRefusedError:
        logger.critical('Подключение не установлено, сервер отверг запрос')


if __name__ == '__main__':
    main()
