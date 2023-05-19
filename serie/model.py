class Serie:
    id: int
    tipo: str
    nombre: str
    imagen: str
    url: str

    def __init__(self, tupla) -> None:
        self.id, self.tipo, self.nombre, self.imagen, self.url = tupla

    def __str__(self) -> str:
        return f'{self.id} {self.tipo} {self.nombre} {self.imagen} {self.url}'
    
    def get(self) -> tuple:
        return (self.tipo, self.nombre, self.imagen, self.url)