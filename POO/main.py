from typing import Protocol

from usuarios import UsuarioProtocol

class LibroProtocol(Protocol):
    disponible: bool              # ← agregar el atributo
    titulo: str                   # ← este también lo usas fuera
    
    def prestar(self) -> str: ...
    def calcular_duracion(self) -> str: ...

class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    def __str__(self):
        return f"{self.titulo} - {self.autor} - ISBN: {self.isbn} - Disponible: {self.disponible}"

    def __repr__(self):
        return self.__str__()

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"{self.titulo}: prestado exitosamente. Total préstamos: {self.__veces_prestado}"
        else:
            return f"El libro {self.titulo} no esta disponible"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} se ha devuelto"
    
    def es_popular(self):
        if self.__veces_prestado > 5:
            return f"{self.titulo} es popular"
        else:
            return f"{self.titulo} no es popular"

    def get_veces_prestado(self):
        return self.__veces_prestado
    
    def set_veces_prestado(self, veces_prestado):
        self.__veces_prestado = veces_prestado            

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
    
class LibroFisico(Libro):
    def __init__(self, titulo, autor, isbn, disponible=True, tapa_dura= True):
        super().__init__(titulo, autor, isbn, disponible)
        self.tapa_dura = tapa_dura
    
    def calcular_duracion(self):
        if self.tapa_dura:
            return f"La duración del préstamo de {self.titulo} es de 30 días"
        else:
            return f"La duración del préstamo de {self.titulo} es de 14 días"
        
class LibroDigital(Libro):
    def __init__(self, titulo, autor, isbn, disponible=True, formato="PDF"):
        super().__init__(titulo, autor, isbn, disponible)
        self.formato = formato
    
    def calcular_duracion(self):
        if self.formato == "PDF":
            return f"La duración del préstamo de {self.titulo} es de 14 días"
        else:  
            return f"La duración del préstamo de {self.titulo} es de 7 días"
    

if __name__ == "__main__":
    libro1 = LibroFisico("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True, True)
    libro2 = LibroDigital("1984", "George Orwell", "978-0-452-28423-4", True, "EPUB")
    libro3 = LibroDigital("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", False, "PDF")

    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.libros = [libro1, libro2, libro3]

    print(biblioteca.libros_disponibles())
