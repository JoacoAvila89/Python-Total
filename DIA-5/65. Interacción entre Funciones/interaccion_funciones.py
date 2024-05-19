from random import shuffle

#lista inicial
lista_palitos = ['|','||','|||','||||']

#funcion mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

# funcion pedir intento
def selecciona_palito():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)

#funcion chequear intento
def chequer_intento(lista,intento):
    if lista[intento - 1]  == '|':
        print("\nMuy de malas compa te toca lavar los platos")
    else:
        print("\nEres un tremendo suertudo")

    print(f"Te ha tocado el {lista[intento-1]}")
    
palitos_mezclados = mezclar(lista_palitos)
seleccion = selecciona_palito()
chequer_intento(palitos_mezclados,seleccion)
