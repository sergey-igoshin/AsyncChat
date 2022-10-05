import json
import socket
from datetime import datetime
import argparse
import select
from queue import Queue, Empty
from server_log_config import logger


MSG_SIZE = 1024
LISTEN_SIZE = 5


def parse_server_arguments():
    parser = argparse.ArgumentParser(description="Сервер")
    parser.add_argument('-a', '--addr', type=str, default='localhost')
    parser.add_argument('-p', '--port', type=int, default=7777)
    return parser.parse_args()


def get_action(data, address):
    if data.get('action') == 'presence':
        return {
            'response': 200,
            'data': {
                'message': f'{data.get("message")}',
                'time': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
            'address': address,
        }
    return {'error': 'Упс, что-то пошло не так'}


def input_output_remove(s, inputs, outputs, message_queues, address):
    inputs.remove(s)
    if s in outputs:
        outputs.remove(s)
    del message_queues[s]
    s.close()
    logger.debug(f"Соединение разорвано с {address}")
    return


def main(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.setblocking(False)
            server.bind((host, port))
            server.listen(LISTEN_SIZE)
            inputs = [server]
            outputs = []
            message_queues = {}
            logger.info('Start')
            while inputs:
                readable, writable, exceptional = select.select(inputs, outputs, inputs)

                for s in readable:
                    if s is server:
                        client, address = s.accept()
                        logger.debug(f"Соединение установлено с {address}")

                        client.setblocking(False)
                        inputs.append(client)
                        message_queues[client] = Queue()
                    else:
                        data = s.recv(MSG_SIZE)
                        if data:
                            message_queues[s].put(data)
                            if s not in outputs:
                                outputs.append(s)
                        else:
                            input_output_remove(s, inputs, outputs, message_queues, address)

                for s in writable:
                    try:
                        request = json.loads(message_queues[s].get_nowait().decode('utf-8'))
                    except Empty:
                        outputs.remove(s)
                    else:
                        response = get_action(request, address)
                        s.send(json.dumps(response).encode('utf-8'))

                for s in exceptional:
                    input_output_remove(s, inputs, outputs, message_queues, address)
    except KeyboardInterrupt:
        logger.critical('Stop')


if __name__ == '__main__':
    args = parse_server_arguments()
    main(host=args.addr, port=args.port)
