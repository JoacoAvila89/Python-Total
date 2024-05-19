def devolver_distintos(num1, num2, num3):
    lista_enteros = [num1, num2, num3]
    suma = sum(lista_enteros)

    if suma > 15:
        return max(lista_enteros)
    elif suma < 10:
        return min(lista_enteros)
    else:
        lista_enteros.sort()
        return lista_enteros[1]

resultado = devolver_distintos(1, 3, 8)
print(resultado)  # True