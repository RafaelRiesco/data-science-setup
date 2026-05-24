class Biblioteca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros: list[LibroProtocol] = []    # ← lista de LibroProtocol
        self.usuarios: list[UsuarioProtocol] = [] # ← lista de UsuarioProtocol}
    
    def libros_disponibles(self):
        return [
        libro.titulo
        for libro in self.libros
        if libro.disponible 
        ]
