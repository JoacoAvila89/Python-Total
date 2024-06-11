"""
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando 
desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

Pista: Utiliza un loop while para realizar este ejercicio."""

def mi_generador():
    i = 1
    while i > 0:
        yield i
        i += 1

g = mi_generador()
print(next(g))
print(next(g))
print(next(g))


