lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

lista2 = ['Jose', 'Liz', 'Delvalle', 'Goyo', 'Gregorio']

for nombres in lista2:
    if nombres.startswith("G"):
        print(nombres)

numeros = [1,2,3,4,5,6,7 ]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)

dic = {'clave1': 'a','clave2':'b','clave3':'c'}

for a,b in dic.items():
    print(a,b)




