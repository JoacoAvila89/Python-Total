
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True

lista_numeros = [1,50,502,5000,755,600,33,-61]
resultado = todos_positivos(lista_numeros)
print(resultado)