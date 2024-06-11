"""
"Son tipos especiales de funciones que devuelven un iterador que no almacena su contenido completo en memoria, sino que "demora" 
la ejecución de una expresión hasta que su valor se solicita."
"""

def mi_funcion():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))
print(next(g))
print(next(g))

def mi_generador_2():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

print("-------------------------------------------------------------------------------")
j = mi_generador_2()
print(next(j))
print(next(j))
print("Esto no interrumpe nada")
print(next(j))
