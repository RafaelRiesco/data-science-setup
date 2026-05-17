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

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0-15-601219-5", False)


libro1.prestar()
libro1.devolver()

libro1.prestar()
libro1.devolver()
print(libro1.prestar())
print(libro1.prestar())
print(libro1.get_veces_prestado())

libro1.set_veces_prestado(10)
print(libro1.get_veces_prestado())