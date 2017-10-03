import logging
import traceback
import json
import os
from datetime import datetime

class Log:

    def __init__(self):
        logging.basicConfig(filename = '_log', level = logging.DEBUG)
        self.shared_instance = logging

    def info(self, file, title, reference, event):
        data = {
            'date'  : datetime.today(),
            'type'  : 'INFO',
            'info'  : reference,
            'event' : event
        }
        self.shared_instance.info(data)

    def debug(self, referece):
        data = {
            'date'  : datetime.today(),
            'type'  : 'DEBUG',
            'info'  : referece
        }
        self.shared_instance.debug(data)

    def warning(self, reference, file, line, error):
        data = {
            'date'  : datetime.today(),
            'type'  : 'WARNING',
            'file'  : file,
            'info'  : reference,
            'line'  : line,
            'error' : error
        }
        self.shared_instance.warning(data)

    def critical(self, error, reference):
        exc_type, exc_value, exc_traceback = error
        lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        data = {
            'date'  : datetime.today(),
            'type'  : 'CRITICAL',
            'info'  : reference,
            'error' : ''.join('!! ' + line for line in lines)
        }
        self.shared_instance.critical(data)
