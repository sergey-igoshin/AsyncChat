import logging
import os


def get_client_filename(filename):
    directory = os.path.dirname(os.path.realpath(__file__))
    log_directory = os.path.join(directory, 'log')
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)
    return os.path.join(log_directory, f'{filename}.log_1')


log_file = get_client_filename('client')

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.FileHandler(log_file, encoding='utf-8')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
