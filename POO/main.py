from exceptions import UsuarioNoEncontradoError
from libros import LibroFisico, LibroDigital
from usuarios import Estudiante, Profesor
from biblioteca import Biblioteca


biblioteca = Biblioteca("Biblioteca Central")

estudiante = Estudiante("Luis", "123456", "Ingeniería")
profesor = Profesor("Ana", "987654")
estudiante2 = Estudiante("Maria", "654321", "Medicina")

libro1 = LibroFisico("Cien años de soledad", "Gabriel García Márquez", "978-0-06-088328-7", True, True)
libro2 = LibroDigital("1984", "George Orwell", "978-0-452-28423-4", True, "EPUB")
libro3 = LibroDigital("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", False, "PDF")

biblioteca.usuarios = [estudiante, profesor, estudiante2]
biblioteca.libros = [libro1, libro2, libro3]


print("Bienvenido a la Biblioteca Central")
print("Libros disponibles:")
for titulo in biblioteca.libros_disponibles():
    print(f"- {titulo}")
    
cedula = input("Ingrese la cédula del usuario: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(f"Usuario encontrado: {usuario.nombre}")
except UsuarioNoEncontradoError as e:
    print(f"Error: {e}")