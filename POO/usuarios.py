from typing import Protocol
from exceptions import TituloInvalidoError
from abc import ABC, abstractmethod

class UsuarioProtocol(Protocol):
    def solicitar_prestamo(self, titulo: str) -> str: 
        ...

class UsuarioBase(ABC):
    @abstractmethod
    def solicitar_prestamo(self):
        pass
    
class Usuario(UsuarioBase):
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_prestamo(self, titulo):
        return f"{self.nombre} ha solicitado el libro '{titulo}'"
    
    def devolver_libro(self, titulo):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"{self.nombre} ha devuelto el libro '{titulo}'"
        else:            
            return f"{self.nombre} no tiene el libro '{titulo}' prestado"
        
class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_prestamos = 3
    
    
    def solicitar_prestamo(self, titulo):
        if not titulo:
            raise TituloInvalidoError("El título del libro no puede ser None")
        if len(self.libros_prestados) < self.limite_prestamos:
            self.libros_prestados.append(titulo)
            return f"{self.nombre} ha solicitado el libro '{titulo}'"
        else:
            return f"{self.nombre} ha alcanzado el límite de préstamos. Limite alcanzado: {self.limite_prestamos}"    

class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None
    
    def solicitar_prestamo(self, titulo):
        self.libros_prestados.append(titulo)
        return f"{self.nombre} ha solicitado el libro '{titulo}'"
    