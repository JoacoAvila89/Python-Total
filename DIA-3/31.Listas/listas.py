mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']

print(mi_lista[0:2])
print(mi_lista + mi_lista2)

mi_lista[0] = 'Avila'
mi_lista2.append('g')

print(mi_lista + mi_lista2)
print(mi_lista2.pop(0))

lista3 = ['g','d','h','p']
lista3.sort()
print(lista3)

lista3.reverse()
print(lista3)