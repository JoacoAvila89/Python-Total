serie = 'N-02'

"""if serie == 'N-01':
    print("Ssmsung")
elif serie == 'N-02':
    print("Nokia")
elif serie == 'N-03':
    print("Motorola")
else:
    print("El producto no existe")"""

#Con el update de python a 3.10
match serie:
    case "N-01":
        print("Ssmsung")
    case 'N-02':
        print("Nokia")
    case 'N-03':
        print("Motorola")
    case _:
        print("El producto no existe")


cliente = {'nombre': 'Joaquin', 'edad': '34', 'ocupacion': 'aprendiz'}
pelicula = {'titulo': 'Harry Potter', 'ficha_tecnica':{'protagonista': 'Daniel Radclife', 'director': 'Morgan Freeman'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre': nombre, 'edad': edad, 'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo': titulo, 'ficha_tecnica': {'protagonista': protagonista, 'director': director}}:
            print("Es una pelicula")
            print(titulo,protagonista,director)
        case _:
            print("No se lo que es")