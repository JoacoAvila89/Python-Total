lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numeros in lista_numeros:
    if numeros%2 == 0:
        suma_pares += numeros
    else:
        suma_impares += numeros

print(suma_impares,suma_pares)