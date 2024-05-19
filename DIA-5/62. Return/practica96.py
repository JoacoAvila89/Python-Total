def invertir_palabra(palabra):
    palabra = palabra[::-1].upper()
    return palabra

palabra = "Aprendizaje"
result = invertir_palabra(palabra)
print(result)