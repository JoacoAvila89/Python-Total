"""
Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""
mi_archivo = open("mi_archivo.txt","w")
mi_archivo.write("Nuevo texto")
mi_archivo.close()

mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())
mi_archivo.close()