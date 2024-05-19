def letras_unicas(palabra):
    palabra_separada = []

    for n in palabra:
        palabra_separada.append(n)
    
    lista_sin_repetidos = list(set(palabra_separada))
    lista_sin_repetidos.sort()

    return lista_sin_repetidos

print(letras_unicas("entretenido"))