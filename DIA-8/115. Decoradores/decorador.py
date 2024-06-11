def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adios")
    return otra_funcion

@decorar_saludo
def mayuscula(texto):
    print(texto.upper())

@decorar_saludo
def minuscula(texto):
    print(texto.lower())

def primera_letra_may(texto):
    print(texto.title())

def intercambia_letra(texto):
    print(texto.swapcase())

#Ejecuta el decorador ya que lo tiene asignado, no se puede en este caso ejecutar solo minuscula a menos que que se le quite decortador
saludo = minuscula("Joaquin")

#Para jugar con el decorador se puede hacer de esta forma, donde se llama a decorar saludo y se le pasa a funcion
intercambio_decorado = decorar_saludo(intercambia_letra)
intercambio_decorado("Barcelona")
