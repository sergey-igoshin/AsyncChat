import json
from socket import socket, AF_INET, SOCK_STREAM
import select
from config import ParseArguments, Logger

l = Logger(filename='server', rotate_on=True)
parse = ParseArguments(description='server')


def get_response(response, alert):
    msg_dict = {
        "response": response,
        "alert": {
            'from': alert['from'],
            'message': alert['message'],
        }
    }
    msg_json = json.dumps(msg_dict)
    return msg_json


def sockets(addr, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)
    sock.settimeout(0.2)
    return sock


def write_client(msg, w, clients):
    for i in w:
        response = get_response("200", msg)
        try:
            i.send(response.encode('utf-8'))
        except Exception as e:
            clients.remove(i)
            l.log().critical(f'write_client {e}')


def read_client(msg, r, clients):
    for i in r:
        try:
            data = i.recv(1024)
            response = json.loads(data.decode('utf-8'))

            if response.get("message") == "exit":
                response['message'] = 'покинул чат'
                request = get_response("200", response)
                i.send(request.encode('utf-8'))
                l.log().critical(f'Покинул чат {i}')
                clients.remove(i)
            msg.append(response)
        except Exception as e:
            clients.remove(i)
            l.log().critical(e)
    return msg


def main_loop():
    addr, port = parse.parse_args()
    try:
        l.log().debug('Start')
        clients = []
        clients_msg = []
        sock = sockets(addr, port)

        while True:
            try:
                conn, address = sock.accept()
                l.log().info(f"{address} подключился к чату")
            except OSError as e:
                pass
            else:
                print(f"{address} подключился к чату")
                clients.append(conn)
            finally:
                r = []
                w = []
                try:
                    r, w, e = select.select(clients, clients, [], 0)
                except Exception as e:
                    pass
                read_client(clients_msg, r, clients)
                for msg in clients_msg:
                    write_client(msg, w, clients)
                clients_msg = []
    except Exception as e:
        l.log().critical(f'Stop {e}')
    except KeyboardInterrupt:
        l.log().critical(f'Stop')


if __name__ == '__main__':
    main_loop()
