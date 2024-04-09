frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase2 = frase.replace("difícil","fácil").replace("mala","buena")
print(frase2)

buscar_palabra = "Python"
dic_palabra = {True:'Si Existe',False:'No Existe'}
validacion = buscar_palabra in frase
resulta = dic_palabra[validacion]
print(f"La palabra {buscar_palabra} {resulta}")
