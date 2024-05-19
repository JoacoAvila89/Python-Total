def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def contar_primos(num):
    cantidad_primos = 0
    primos_encontrados = []
    for i in range(2, num + 1):
        if es_primo(i):
            primos_encontrados.append(i)
            cantidad_primos += 1
            print(i, end=' ')
    print()  # Para imprimir un salto de línea después de los números primos encontrados
    return cantidad_primos

# Ejemplo de uso:
numero_limite = 20
cantidad_primos_encontrados = contar_primos(numero_limite)
print(f"Se encontraron {cantidad_primos_encontrados} números primos hasta {numero_limite}.")
