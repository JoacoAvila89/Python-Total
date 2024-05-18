from random import *

# numeros enteros del 1 al 60
aleatorio = randint(1,60)
print(aleatorio)

# numeros con 2 decimales desde el 1 al 5
aleatorio = round(uniform(1,5),2)
print(aleatorio)

#numero decimal entre el 0 y 2
aleatorio = random()
print(aleatorio)

#escoger una opcion aleatoria de una lista
colores = ['azul','amarillo','verde','morado']
aleatorio = choice(colores)
print(aleatorio)

#numeros dentro de un rango, desde 5 al 50.
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)