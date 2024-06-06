"""Práctica Métodos Especiales 1
Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", 
de {autor}' (atención: el título debe estar encerrado entre comillas dobles)."""
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self) -> str:
        return f'"{self.titulo}", de {self.autor}'

harry = Libro("prisionero", "jose", 456)
print(harry)