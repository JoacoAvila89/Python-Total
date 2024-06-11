
def decorador_mensaje(opcion):
        
        print("Su turno es: ")
        if opcion == 'P':
            print(next(p))
        elif opcion == 'F':
            print(next(f))
        else:
            print(next(c))
        print("Aguarde y sera atendido")


def generador_farmacia():
    i = 1   
    while True:
        yield f"F-{i}"
        i += 1


def generador_perfumeria():
    i = 1 
    while True:
        yield f"P-{i}"
        i += 1


def generador_cosmeticos():
    i = 1 
    while True:
        yield f"C-{i}"
        i += 1


c = generador_cosmeticos()
p = generador_perfumeria()
f = generador_farmacia()
