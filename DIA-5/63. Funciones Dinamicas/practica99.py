"""Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y
 devuelva el resultado de dicha cuenta.

"""

def cantidad_pares(lista_numeros):
    lista_pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            pass
    return len(lista_pares)

lista_numeros = [5,6,9,1000,0,0,8,20]
resultado = cantidad_pares(lista_numeros)
print(resultado)
