from typing import Protocol
from exceptions import LibroNoDisponibleError

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
        if not self.disponible:
            raise LibroNoDisponibleError(f"El libro {self.titulo} no está disponible")
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
    
