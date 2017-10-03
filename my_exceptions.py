import my_logging

class CriticalError(Exception):
    '''
        For custom errors

        Attributes:
            Exception - Exception of the error
    '''

    __log = my_logging.Log()

    def __init__(self, message, error):
        self.message = message