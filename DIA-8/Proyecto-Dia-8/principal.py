import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            opcion_elegida = input("Elija su rubro: ").upper()
            ["P", "F", "C"].index(opcion_elegida)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            break

    numeros.decorador_mensaje(opcion_elegida)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Esa no es una opción válida")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
