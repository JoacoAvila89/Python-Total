def suma():
    n1 = int(input("numero 1: "))
    n2 = int(input("numero 2: "))
    print(n1+n2)
    print("Gracias por sumar" + n1 + "<-- para prueba de TypeError")

try:
    suma()
except ValueError:
    print("Ese no es un número")
except TypeError:
    print("Estas intentando contanenar tipos distintos")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo compa!!!")

"""
try:
    #Codigo que queremos probar
except:
    #codigo a ejecurar si hay un error
else:
    #codigo a ejecurar si no hay un error
finally:
    #codigo que se va a ejecutar de todos modos
"""

def pedirNumero():

    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el número {numero}")
            break
    print("Gracias!!!")