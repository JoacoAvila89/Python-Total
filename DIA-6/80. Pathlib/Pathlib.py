from pathlib import Path

carpeta = Path("C:/Users/jjoaq/OneDrive/Documentos/prueba-curso-python.txt")
print(carpeta.read_text())
print(carpeta.stem)
print(carpeta.suffix)
print(carpeta.anchor)
print(carpeta.name)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Archivo si existe")