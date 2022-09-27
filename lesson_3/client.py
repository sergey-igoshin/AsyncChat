import socket
import json
import argparse


def parse_client_arguments():
    parser = argparse.ArgumentParser(description="Клиент")
    parser.add_argument('-a', '--addr', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)
    return parser.parse_args()


def message_dumps(**kwargs):
    return json.dumps(kwargs)


def get_response(data):
    if data.get('response') == 200:
        return f"{data.get('data')['message']} {data.get('data')['time']}"
    return data.get('error')


def main(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
        clientsocket.connect((host, port))

        while True:
            message = input('> ')
            MSG = message_dumps(
                action='presence',
                message=message,
            )
            clientsocket.send(MSG.encode())
            data = clientsocket.recv(1024)
            response = json.loads(data.decode('utf-8'))
            print(get_response(response))


if __name__ == '__main__':
    args = parse_client_arguments()
    main(host=args.addr, port=args.port)
