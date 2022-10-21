import argparse
import logging
from logging.handlers import TimedRotatingFileHandler
import os


class ParseArguments:
    def __init__(self, description):
        self.parse = argparse.ArgumentParser(description=description)

    def parse_args(self):
        self.parse.add_argument('-a', '--addr', type=str, default='localhost')
        self.parse.add_argument('-p', '--port', type=int, default=7777)
        return self.parse.parse_args().addr, self.parse.parse_args().port


class Logger:
    def __init__(self, filename, rotate_on):
        self.filename = filename
        self.rotate = rotate_on
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.logger = logging.getLogger()
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    def get_filename(self):
        log_directory = os.path.join(self.directory, 'log')
        if not os.path.exists(log_directory):
            os.mkdir(log_directory)

        if self.rotate:
            date = os.path.splitext(self.filename)[1][1:]
            if date:
                rotating_filename = os.path.join(log_directory, date)
                return f'{rotating_filename}.log'

        return os.path.join(log_directory, f'{self.filename}.log')

    def log(self):
        log_file = self.get_filename()

        if self.rotate:
            handler = TimedRotatingFileHandler(log_file, encoding='utf-8', when='midnight', interval=1, backupCount=0)
            handler.suffix = '%d%m%Y'
            handler.namer = self.get_filename
        else:
            handler = logging.FileHandler(log_file, encoding='utf-8')

        handler.setFormatter(self.formatter)
        handler.setLevel(logging.DEBUG)

        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
        return self.logger
