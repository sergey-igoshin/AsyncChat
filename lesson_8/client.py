import json
import time
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from config import ParseArguments, Logger

parse = ParseArguments(description='client')
l = Logger(filename='client', rotate_on=False)


def create_msg(name, message):
    msg_dict = {
        "action": "msg",
        "time": time.time(),
        "to": "#room_name",
        "from": name,
        "message": message
    }
    msg_json = json.dumps(msg_dict)
    return msg_json


def send_msg(sock, name):
    sock.send(create_msg(name, 'подключился к чату').encode("utf-8"))
    while True:
        try:
            message = input("")
            request = create_msg(name, message)
            sock.send(request.encode("utf-8"))
            l.log().info(request)

        except Exception:
            pass


def read_msg(sock, name):
    while True:
        try:
            data = sock.recv(1024)
            response = json.loads(data.decode('utf-8'))
            if name != response['alert']['from']:
                print(f"от {response['alert']['from']}: {response['alert']['message']}")

        except Exception:
            pass


def main():
    addr, port = parse.parse_args()
    try:
        print("Для подключения к чату представьтесь")
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((addr, port))
            name = input("> ")
            l.log().debug('Установлено соединение с сервером')
            ts = Thread(target=send_msg, args=(sock, name), daemon=True)
            tr = Thread(target=read_msg, args=(sock, name), daemon=True)
            ts.start()
            tr.start()
            ts.join()
            tr.join()
    except KeyboardInterrupt:
        l.log().critical('Соединение с сервером разорвано')
    except ConnectionRefusedError:
        l.log().critical('Подключение не установлено, сервер отверг запрос')


if __name__ == '__main__':
    main()
