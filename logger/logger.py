import logging

formatter = logging.Formatter("%(asctime)s %(levelname)s --- %(message)s", "%Y-%m-%d %H:%M:%S")
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(formatter)

class CustomLogger:
    logger: logging.Logger

    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(consoleHandler)

    def info(self, texto):
        self.logger.info(f'{texto}')

    def error(self, texto):
        self.logger.error(f'{texto}')

    def warn(self, texto):
        self.logger.warn(f'{texto}')

    def debug(self, texto):
        self.logger.debug(f'{texto}')