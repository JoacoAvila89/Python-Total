def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(300)
print(resultado)

def chequear_3_cifras_2(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras_2([3000,55,2200])
print(resultado)

def chequear_3_cifras_3(lista):
    lista_3_cifras = []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras_3([300,55,220])
print(resultado)