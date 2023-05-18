class MockService:
    mock_name: str

    def __init__(self, mock_name) -> None:
        self.mock_name = mock_name

    def write(self, content_file):
        with open(self.mock_name, "w") as file:
            file.write(content_file)
            
    def read(self):
        with open(self.mock_name, "r") as file:
            content_file = file.read()
        return content_file
    
    def append(self):
        with open(self.mock_name, "a") as file:
            content_file = file.read()
        return content_file