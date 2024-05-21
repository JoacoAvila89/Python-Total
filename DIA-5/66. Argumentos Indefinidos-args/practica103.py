"""Práctica sobre Argumentos Indefinidos (*args) 1
Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).
"""

lista_numeros= [1,5,6,8]
def suma_cuadrados(*args):
    suma = 0
    for num in args:
        suma += num**2
    return suma