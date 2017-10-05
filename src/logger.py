import inspect
from os import environ

class Logger:
    def log(message):
        '''Print a message with location information'''
        if environ.get('env') != 'PROD':
            func = inspect.currentframe().f_back.f_code
            print("%s:%s->%s->%s" % (
                func.co_filename.split('/').pop(),
                func.co_firstlineno,
                func.co_name,
                message,
            ))