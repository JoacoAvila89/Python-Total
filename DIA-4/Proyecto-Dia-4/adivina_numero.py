from random import *

numero = randint(1,100)
intentos = 0
nombre = input("Hola, ¿Cual es tu nombre? ")

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número. \nComencemos!!!")

while intentos < 8:
    valor_ingresado = int(input("¿Cual es el número: "))
    intentos+= 1
            
    if valor_ingresado == numero:
        print(f"Eres un crack, haz adivinado el número {numero} en {intentos} intentos")
        break
    elif valor_ingresado > 100 or valor_ingresado < 1:
        print("Haz elegido un número que no está permitido")
    elif valor_ingresado < numero:
        print("Su respuesta es incorrecta ya que ha elegido un número menor al número secreto")
    elif valor_ingresado > numero:
        print("Su respuesta es incorrecta ya que ha elegido un número mayor al número secreto")    

if valor_ingresado != numero:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero}")    
    