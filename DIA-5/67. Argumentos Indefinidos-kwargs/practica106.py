"""
Práctica sobre Argumentos Indefinidos (**kwargs) 1
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
"""

def cantidad_atributos(**kwargs):
    lista_atributos = []
    for parametro in kwargs.items():
        lista_atributos.append(parametro)
    return len(lista_atributos)

kwargs = {'1': 'uno','2':'dos', '3': 'tres', '4':'cuatro' }
print(cantidad_atributos(**kwargs))   


        