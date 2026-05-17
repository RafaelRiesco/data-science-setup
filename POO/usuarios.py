from typing import Protocol

class UsuarioProtocol(Protocol):
    def solicitar_prestamo(self, titulo: str) -> str: 
        ...

class Usuario:
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
    

from main import Libro
estudiante = Estudiante("Luis", "123456", "Ingeniería")
profesor = Profesor("Ana", "987654")
estudiante2 = Estudiante("Maria", "654321", "Medicina")
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True)

usuarios : list[UsuarioProtocol] = [estudiante, profesor, estudiante2, libro1]

for usuario in usuarios:
   print(usuario.solicitar_prestamo("1984"))