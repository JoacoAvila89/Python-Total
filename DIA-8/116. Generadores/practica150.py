"""
Práctica Generadores 3
Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
Almacena el generador en la variable perder_vida"""

def mi_generador():
    vidas = 3

    yield f"Te quedan {vidas} vidas"
    vidas -= 1

    yield f"Te quedan {vidas} vidas"
    vidas -= 1

    yield f"Te queda {vidas} vida"
    vidas -= 1

    yield f"Game Over"

    
perder_vida = mi_generador()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))