from libros import LibroFisico, LibroDigital
from usuarios import Estudiante, Profesor, UsuarioProtocol
from biblioteca import Biblioteca

biblioteca = Biblioteca("Biblioteca Central")

estudiante = Estudiante("Luis", "123456", "Ingeniería")
profesor = Profesor("Ana", "987654")
estudiante2 = Estudiante("Maria", "654321", "Medicina")

usuarios : list[UsuarioProtocol] = [estudiante, profesor, estudiante2]


libro1 = LibroFisico("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True, True)
libro2 = LibroDigital("1984", "George Orwell", "978-0-452-28423-4", True, "EPUB")
libro3 = LibroDigital("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", False, "PDF")

biblioteca.libros = [libro1, libro2, libro3]

print(biblioteca.libros)
