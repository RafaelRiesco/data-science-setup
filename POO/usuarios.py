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
    

estudiante = Estudiante("Luis", "123456", "Ingeniería")
profesor = Profesor("Ana", "987654")

# Pruebas de préstamo
print(estudiante.solicitar_prestamo("El principito"))
print(estudiante.solicitar_prestamo("1984"))
print(estudiante.solicitar_prestamo("El quijote"))
print(estudiante.solicitar_prestamo("La biblia"))

print(profesor.solicitar_prestamo("El principito"))
print(profesor.solicitar_prestamo("1984"))
print(profesor.solicitar_prestamo("El quijote"))
print(profesor.solicitar_prestamo("La biblia"))

print(estudiante.devolver_libro("El principito"))
print(estudiante.devolver_libro("1984"))

print(len(estudiante.libros_prestados))  # Debe ser 3
print(len(profesor.libros_prestados))    # Debe ser 4