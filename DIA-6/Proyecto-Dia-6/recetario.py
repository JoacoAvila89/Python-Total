from pathlib import Path

base = Path.home()
ruta = Path(base, "Python-Total", "DIA-6","Proyecto-Dia-6","Recetas")

lista_categorias = [item for item in ruta.iterdir() if item.is_dir()]
lista_recetas = list(ruta.glob("**/*.txt"))

nombre = input("Ingresa tu nombre: ")
print(f"Bienvenido {nombre},\nlas recetas se encuentran en {ruta}")
print(f"Actualmente contamos con {len(lista_recetas)} recetas")
print("\n****Menu *****")
menu_principal = {1:'Leer Receta', 2:'Crear Receta', 3:'Crear Categoría', 4:'Eliminar Receta', 5:'Eliminar Categoría', 6: 'Finalizar Programa'}


def mostrar_menu():
    esValido = False
    opciones = '123456'

    while not esValido:
        for id,opcion in menu_principal.items():
            print(f"[{id}] - {opcion}")
        id = input("Elige una opcion: ")
        if id in opciones and len(id) == 1:
            esValido = True
        else:
            print("No has elegido una opción correcta")
    return id

def elegir_categoria(opcion):
    esValido = False
   

    if opcion == '1':

        while not esValido:
            print("****Categorias *****\n")
            for i, categoria in enumerate(lista_categorias, start=1):
                print(f"[{i}] - {categoria.name}")

            try:
                eleccion_categoria = int(input("¿Qué opción prefieres?: "))
                if 1 <= eleccion_categoria <= len(lista_categorias):
                    esValido = True
                    receta_seleccionada = mostrar_recetas(lista_categorias[eleccion_categoria - 1].name)
                    print(leer_receta(receta_seleccionada,lista_categorias[eleccion_categoria - 1].name))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

    elif opcion == '2':
        while not esValido:
            print("****Categorias *****\n")
            for i, categoria in enumerate(lista_categorias, start=1):
                print(f"[{i}] - {categoria.name}")
            try:
                eleccion_categoria = int(input("Sobre que categoria quieres crear una receta: "))
                if 1 <= eleccion_categoria <= len(lista_categorias):
                    esValido = True
                    categoria_seleccionada = lista_categorias[eleccion_categoria - 1].name
                    crear_receta(categoria_seleccionada)
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

    elif opcion == '3':
        crear_categoria()

    elif opcion == '4':
        while not esValido:
            print("****Categorias *****\n")
            for i, categoria in enumerate(lista_categorias, start=1):
                print(f"[{i}] - {categoria.name}")
        
            try:
                eleccion_categoria = int(input("Sobre que categoria quieres eliminar una receta: "))
                if 1 <= eleccion_categoria <= len(lista_categorias):
                    esValido = True
                    categoria_seleccionada = lista_categorias[eleccion_categoria - 1].name
                    eliminar_receta(categoria_seleccionada)
                else:
                    print("Número de categoria invalida")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

    elif opcion == '5':
        while not esValido:
            print("****Categorias *****\n")
            for i, categoria in enumerate(lista_categorias, start=1):
                print(f"[{i}] - {categoria.name}")
            try:
                eleccion_categoria = int(input("Ingrese el número de categoria que desea eliminar: "))
                if 1 <= eleccion_categoria <= len(lista_categorias):
                    esValido = True
                    categoria_seleccionada = lista_categorias[eleccion_categoria - 1].name
                    eliminar_categoria(categoria_seleccionada)
                else:
                    print("Categoría no existe")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
    elif opcion == '6':
        exit()
    
    else:
        print("Elige una opcion correcta")

def mostrar_recetas(categoria_seleccionada):
    esValido = False
    ruta_categoria = ruta / categoria_seleccionada
    recetas = [archivo.stem for archivo in ruta_categoria.iterdir() if archivo.suffix == '.txt']
    
    while not esValido:
        if recetas:
            print(f"Recetas de la categoría '{categoria_seleccionada}':")
            for id,receta in enumerate(recetas, start=1):
                print(f"[{id}]- {receta}")

            try:
                eleccion_receta = int(input("Cual receta quieres ver: "))
                if 1 <= eleccion_receta <= len(recetas):
                    esValido = True
                    return recetas[eleccion_receta-1]
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")
        else:
            print("No hay recetas en esta categoría.")  

def leer_receta(receta_seleccionada, categoria_seleccionada):
   ruta_receta = ruta / categoria_seleccionada / (receta_seleccionada + '.txt') 
   ver_receta = open(ruta_receta)
   return ver_receta.read()

    
def crear_receta(categoria_seleccionada):
    ruta_categoria = ruta / categoria_seleccionada
    recetas = [archivo.stem for archivo in ruta_categoria.iterdir() if archivo.suffix == '.txt']

    nombre_receta = input("Como se llama la receta: ")
    descripcion_receta = input("Que contiene la receta: ")

    ruta_nueva_receta = ruta_categoria / (nombre_receta + '.txt')

    try:
        with open(ruta_nueva_receta, 'w') as archivo_receta:
            archivo_receta.write(descripcion_receta)
            archivo_receta.close
        print("La receta se ha creado correctamente.")
    except Exception as e:
        print(f"No se pudo crear la receta. Error: {e}")

def crear_categoria():
    nombre_categoria = input("Ingrese el nombre de la nueva categoría: ")

    ruta_nueva_categoria = ruta / nombre_categoria

    try:
        ruta_nueva_categoria.mkdir()
        print("La categoría se ha creado correctamente.")
    except Exception as e:
        print(f"No se pudo crear la categoría. Error: {e}")

def eliminar_receta(categoria_seleccionada):
    esValido = False
    ruta_categoria = ruta / categoria_seleccionada
    recetas = [archivo.stem for archivo in ruta_categoria.iterdir() if archivo.suffix == '.txt']
    while not esValido:
        if recetas:
            print(f"Recetas de la categoría '{categoria_seleccionada}':")
            for id, receta in enumerate(recetas, start=1):
                print(f"[{id}]- {receta}")

            try:    
                numero_receta = int(input("¿Cual receta quieres eliminar: "))
                if 1 <= numero_receta <= len(recetas):
                    esValido = True
                    ruta_receta = ruta_categoria / (recetas[numero_receta-1]+ ".txt")

                    if ruta_receta.exists():
                        try:
                            ruta_receta.unlink()
                            print("La receta se ha eliminado correctamente.")
                        except Exception as e:
                            print(f"No se pudo eliminar la receta. Error: {e}")
                    else:
                        print("La receta no existe en esta categoría.")

                else:
                    print("Número de receta invalido")
            except ValueError:
                print("Por favor, ingresa un número entero válido.")

        else:
            print("No hay recetas en esta categoría.")
            break

def eliminar_categoria(nombre_categoria):
    ruta_categoria = ruta / nombre_categoria

    if ruta_categoria.exists():
        try:
            ruta_categoria.rmdir()
            print("La categoría se ha eliminado correctamente.")
        except Exception as e:
            print(f"No se pudo eliminar la categoría. Error: {e}")
    else:
        print("La categoría no existe.")

opcion_elegida = mostrar_menu()
elegir_categoria(opcion_elegida)
