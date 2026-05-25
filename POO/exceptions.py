class BibliotecaError(Exception):
    """Excepción base para errores relacionados con la biblioteca."""
    pass

class TituloInvalidoError(BibliotecaError):
    """Excepción para títulos de libros inválidos."""
    pass

class LibroNoDisponibleError(BibliotecaError):
    """Excepción para libros no disponibles."""
    pass