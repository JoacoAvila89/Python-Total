"""Aplica un Counter (contador) sobre la lista de números entregada a continuación, 
y almacénalo en una variable llamada contador"""

from collections import Counter
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)

# Obtener la frecuencia del número 1
frecuencia_numero_1 = contador[1]
print(f"El número 1 está repetido {frecuencia_numero_1} veces.")

# Obtener los elementos ordenados de mayor a menor frecuencia
ordenados_por_frecuencia = contador.most_common()

print("Elementos ordenados por frecuencia de mayor a menor:")
for elemento, frecuencia in ordenados_por_frecuencia:
    print(f"Elemento {elemento} tiene {frecuencia} ocurrencias.")

# Obtener el elemento que se repite más veces
elemento_mas_comun = contador.most_common(1)[0][0]

print(f"El número que se repite más veces es: {elemento_mas_comun}")