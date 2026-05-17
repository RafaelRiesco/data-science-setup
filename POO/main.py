historial_prestamos = []

class Libro:
    def __init__(self, titulo, autor, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    def __str__(self):
        return f"{self.titulo} - {self.autor} - ISBN: {self.isbn} - Disponible: {self.disponible}"

    def __repr__(self):
        return self.__str__()

    def prestar(self):
        if self.disponible:
            self.disponible = False
            historial_prestamos.append(self)
            return f"{self.titulo}: prestado exitosamente."
        else:
            return f"El libro {self.titulo} no esta disponible"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} se ha devuelto"
    
    def es_popular(self):
        if historial_prestamos.count(self) > 5:
            return f"{self.titulo} es popular"
        else:
            return f"{self.titulo} no es popular"

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-15-601219-5", False)

libro1.prestar()
libro1.devolver()

libro1.prestar()
libro1.devolver()

print(historial_prestamos.count(libro1))