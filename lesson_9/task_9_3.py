"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).
Таблица должна состоять из двух колонок и выглядеть примерно так:

Reachable         Unreachable
-------------     -------------
10.0.0.1          10.0.0.3
10.0.0.2          10.0.0.4
"""
from tabulate import tabulate
from task_9_2 import host_range_ping


def host_range_ping_tab(hosts):
    print(tabulate(host_range_ping(hosts, tab=True), headers='keys'))


if __name__ == '__main__':
    host_range_ping_tab(['192.168.0.7', '192.168.0.1'])
