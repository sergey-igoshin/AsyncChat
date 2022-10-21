"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение.
"""


import ipaddress
from task_9_1 import host_ping


def host_range_ping(hosts, tab=False):
    try:
        start, end = sorted((ipaddress.ip_address(i) for i in hosts))
    except Exception as e:
        print(e)
        return

    list_table = []
    while start <= end:
        list_table.append(start)
        start += 1

    return (i for i in host_ping(list_table, tab))


if __name__ == '__main__':
    host_range_ping(['192.168.0.10', '192.168.0.5'])
