from .LoggerFactory import LoggerFactory

class CustomLogger:
    def __init__(self, logger_path) -> None:
        self.debug_factory = LoggerFactory.get_logger(f"{logger_path}/debug.log", level="debug")
        self.info_factory = LoggerFactory.get_logger(f"{logger_path}/info.log", level="info")
        self.warning_factory = LoggerFactory.get_logger(f"{logger_path}/warning.log", level="warning")
        self.error_factory = LoggerFactory.get_logger(f"{logger_path}/error.log", level="error")
        self.critical_factory = LoggerFactory.get_logger(f"{logger_path}/critical.log", level="critical")
        self.data_factory = LoggerFactory.get_logger(f"{logger_path}/data.log", level="info")
        pass

    def debug(self, message):
        self.debug_factory.debug(message)

    def info(self, message):
        self.info_factory.info(message)

    def warning(self, message):
        self.warning_factory.warning(message)

    def error(self, message):
        self.error_factory.error(message)

    def critical(self, message):
        self.critical_factory.critical(message)

    def data(self, message):
        self.data_factory.info(message)


