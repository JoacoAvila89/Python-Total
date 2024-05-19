def cero_repetido(*args):
    lista = list(args)
    longitud = len(lista)

    for n in range(longitud-1):
        if lista[n] == lista[n+1]:
            return True
       
    return False

print(cero_repetido(5,6,1,4,0,9,0,1))
