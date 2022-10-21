"""
Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
ip_address().
"""

import ipaddress
import subprocess


def host_ping(hosts, tab=False):
    list_table = []
    for host in hosts:
        try:
            ip = ipaddress.ip_address(host)
        except Exception:
            ip = host

        command = ['ping', '-n', '1', str(ip)]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if tab:
            header = 'Reachable' if response.returncode == 0 else 'Unreachable'
            list_table.append({header: ip})
        else:
            result = 'Узел доступен' if response.returncode == 0 else 'Узел не доступен'
            print(f'{host}: {result}')

    return list_table


h = [
    '8.8.8.8',
    'google.com',
    '192.168.0.1',
    'localhost',
    'local',
    '127.0.0.1',
    'vk.ru'
]

if __name__ == '__main__':
    host_ping(h)
