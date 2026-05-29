from exceptions import LibroNoDisponibleError, UsuarioNoEncontradoError
from usuarios import  Profesor
from biblioteca import Biblioteca
from data import data_libros, data_estudiantes

biblioteca = Biblioteca("Biblioteca Central")

profesor = Profesor("Ana", "987654")

biblioteca.usuarios = [profesor] + data_estudiantes
biblioteca.libros = data_libros


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

titulo = input("Ingrese el título del libro que desea buscar: ")
try:    
    libro = biblioteca.buscar_libro(titulo)
    print(f"Libro encontrado: {libro.titulo} por {libro.autor}")
except LibroNoDisponibleError as e:
    print(f"Error: {e}")

resultado = usuario.solicitar_prestamo(titulo)
print(resultado)

try:
    resultado_prestamo = libro.prestar()
    print(resultado_prestamo)
except LibroNoDisponibleError as e:
    print(f"Error: {e}")