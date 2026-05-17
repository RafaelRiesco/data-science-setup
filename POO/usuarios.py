class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_prestamo(self, titulo):
        return f"{self.nombre} ha solicitado el libro '{titulo}'"
        
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
            return f"{self.nombre} ha alcanzado el límite de préstamos. Limite alcanzado: {self.limite_prestamos}."

class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_prestamos = None
    
    def solicitar_prestamo(self, titulo):
        self.libros_prestados.append(titulo)
        return f"{self.nombre} ha solicitado el libro '{titulo}'"
    

estudiante = Estudiante("Luis", "123456", "Ingeniería")
profesor = Profesor("Ana", "987654")

# Pruebas de préstamo
print(estudiante.solicitar_prestamo("Python básico"))
print(estudiante.solicitar_prestamo("Python intermedio"))
print(estudiante.solicitar_prestamo("Python avanzado"))
print(estudiante.solicitar_prestamo("Python Django"))  # Debe indicar límite alcanzado: 3

print(profesor.solicitar_prestamo("Python básico"))
print(profesor.solicitar_prestamo("Python intermedio"))
print(profesor.solicitar_prestamo("Python avanzado"))
print(profesor.solicitar_prestamo("Python Django"))

print(len(estudiante.libros_prestados))  # Debe ser 3
print(len(profesor.libros_prestados))    # Debe ser 4