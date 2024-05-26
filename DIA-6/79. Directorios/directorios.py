import os

ruta = os.getcwd()

#Para cambiar de directorio
ruta = os.chdir("C:\\Users\\jjoaq\\OneDrive\\Documentos")

archivo = open('prueba-curso-python.txt')
print(archivo.read())

#-------------------------------------------------------------

ruta2 = "C:\\Users\\jjoaq\\OneDrive\\Documentos\\prueba-curso-python.txt"

elemento = os.path.basename(ruta2)
print(elemento)

elemento2 = os.path.abspath(ruta2)
print(elemento2)

elemento2 = os.path.split(ruta2)
print(elemento2)
