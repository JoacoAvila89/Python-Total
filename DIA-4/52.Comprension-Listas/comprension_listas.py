palabra = 'Joaquin'
lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

lista2 = [letra for letra in palabra]
print(lista2)

lista3 = [n for n in range(0,21,2) if n*2 > 10]
print(lista3)
#Si a lo anterior se quiere agregar un else:
lista4 = [n if n*2 > 10 else 'no' for n in range(0,21,2) ]
print(lista4)

pies = [10,20,30,40,50]

metros = [n/3.281 for n in pies]
print(metros)