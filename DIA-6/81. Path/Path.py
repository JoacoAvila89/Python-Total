from pathlib import Path

base = Path.home()
print(base)

guia = Path(base, "Barcelona", "Sagrada_Familia.txt")
print(guia)

guia2 = guia.with_name("La_Pedrera.txt")
print(guia2)

print(guia.parent.parent)

#---------------------------------------------------------------------

guia3 = Path(Path.home(), "Python-Total","DIA-6","81. Path","Europa")

for txt in guia3.glob("**/*.txt"):
    print(txt)

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)