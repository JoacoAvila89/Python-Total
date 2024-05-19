"""Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y 
cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma."""

def suma_menores(lista):
    lista_menores = []
    for numero in lista:
        if numero in range(1,1000):
            lista_menores.append(numero)
        else:
            pass
    return sum(lista_menores)

lista_numeros = [5,6,9,1000,0]
resultado = suma_menores(lista_numeros)
print(resultado)

