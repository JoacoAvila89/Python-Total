texto = input("Ingrese un texto, frase o lo que desee: ")
texto_en_minuscula = texto.lower()
lista_letras = list(input("Indiqueme 3 letras: ").lower())

letra1 = texto_en_minuscula.count(lista_letras[0])
letra2 = texto_en_minuscula.count(lista_letras[1])
letra3 = texto_en_minuscula.count(lista_letras[2])
print(f"La primera letra se encuentra: {letra1} veces, la segunda letra se enceuntra: {letra2} veces, y la tercera letra {letra3} veces")

lista_texto = list(texto.split(" "))
cantidad_palabras = len(lista_texto)
print(f"La frase ingresada tiene {cantidad_palabras} palabras")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra es {primera_letra} , la ultima letra es {ultima_letra}")

lista_texto.reverse()
print(" ".join(lista_texto))

dic_palabra = {True:'Si Existe',False:'No Existe'}
validacion = "Python" in texto
resultado = dic_palabra[validacion]
print(f"La palabra Python {resultado} en el texto ingresado")


