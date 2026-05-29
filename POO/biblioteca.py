from libros import LibroProtocol
from usuarios import UsuarioProtocol
from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError

class Biblioteca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros: list[LibroProtocol] = []    # ← lista de LibroProtocol
        self.usuarios: list[UsuarioProtocol] = [] # ← lista de UsuarioProtocol}
    
    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(f"Usuario con cédula {cedula} no encontrado")
    
    def agregar_libro(self, libro: LibroProtocol) -> None:
        self.libros.append(libro)

    def buscar_libro(self, titulo) -> LibroProtocol:
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                return libro
        raise LibroNoDisponibleError(f"Libro con título '{titulo}' no disponible")