"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
"""

import subprocess

SITES = ['yandex.ru', 'youtube.com']


def ping_sites(sites):
    for i in sites:
        args = ['ping', i]
        ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in ping.stdout:
            print(line.decode('cp866').encode('utf-8').decode('utf-8'))


ping_sites(SITES)
