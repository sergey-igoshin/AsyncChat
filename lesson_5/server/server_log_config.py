import logging
from logging.handlers import TimedRotatingFileHandler
import os


def get_server_filename(filename):
    directory = os.path.dirname(os.path.realpath(__file__))
    log_directory = os.path.join(directory, 'log')
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)

    date = os.path.splitext(filename)[1][1:]
    if date:
        rotating_filename = os.path.join(log_directory, date)
        return f'{rotating_filename}.log_1'

    return os.path.join(log_directory, f'{filename}.log_1')
    # if not os.path.exists(f'{filename}.log_1'):
    #     return f'{filename}.log_1'
    #
    # index = 0
    # rotating_filename = f'{filename}.{index}.log_1'
    # while os.path.exists(rotating_filename):
    #     index += 1
    #     rotating_filename = f'{filename}.{index}.log_1'
    # return rotating_filename


log_file = get_server_filename('server')

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

handler = TimedRotatingFileHandler(log_file, encoding='utf-8', when='midnight', interval=1, backupCount=0)
handler.suffix = '%d%m%Y'
handler.namer = get_server_filename

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
