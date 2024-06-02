import logging
from logging import handlers

class LoggerFactory(object):
    _LOG = None

    @staticmethod
    def __create(filename, level, when, backCount):
        """
        A private method that interacts with the python
        logging module
        """
        level_relations = {
            'debug': logging.DEBUG,
            'info': logging.INFO,
            'warning': logging.WARNING,
            'error': logging.ERROR,
            'critical': logging.CRITICAL
        }  # relationship mapping
        # set the logging format
        # log_format = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        log_format = '%(asctime)s:%(levelname)s:%(message)s'
        LoggerFactory._LOG = logging.getLogger(filename)
        format_str = logging.Formatter(log_format)  # Setting the log format
        LoggerFactory._LOG.setLevel(level_relations.get(level))  # Setting the log level
        stream_handler = logging.StreamHandler()  # on-screen output
        stream_handler.setFormatter(format_str)  # Setting the format
        LoggerFactory._LOG.addHandler(stream_handler)
        time_rotating_handler = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,encoding='utf-8')  # automatically generates the file at specified intervals
        time_rotating_handler.setFormatter(format_str)  # Setting the format
        LoggerFactory._LOG.addHandler(time_rotating_handler)
        return LoggerFactory._LOG
    
    @staticmethod
    def get_logger(filename, level='info', when='D', backCount=3):
        """
        A static method called by other modules to initialize logger in
        their own module
        """
        logger = LoggerFactory.__create(filename, level, when, backCount)
        # return the logger object
        return logger