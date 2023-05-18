import logging

formatter = logging.Formatter("%(asctime)s %(levelname)s [%(module)s.%(lineno)d] %(message)s", "%Y-%m-%d %H:%M:%S")
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(formatter)

class CustomLogger:
    logger: logging.Logger

    def __init__(self) -> None:
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(consoleHandler)