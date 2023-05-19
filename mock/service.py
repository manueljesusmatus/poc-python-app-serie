from logger.logger import CustomLogger

class MockService:
    logger: CustomLogger
    mock_name: str

    def __init__(self, mock_name) -> None:
        self.logger = CustomLogger(__name__)
        self.mock_name = mock_name

    def write(self, content_file):
        self.logger.logger.info("Escribiendo archivo mock")
        with open(self.mock_name, "w") as file:
            file.write(content_file)
            
    def read(self):
        self.logger.logger.info("Leyendo archivo mock")
        with open(self.mock_name, "r") as file:
            content_file = file.read()
        return content_file
    
    def append(self):
        self.logger.logger.info("Actualizando archivo mock")
        with open(self.mock_name, "a") as file:
            content_file = file.read()
        return content_file