class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
    
    def __str__(self):
        return f"Album: {self.titulo} tiene como autor a {self.autor} y tiene {self.canciones} canciones"
    
    def __del__(self):
        print("Se ha eliminado el CD")

mi_cd = CD("Canserbero", "Vida-Muerte", 12)
print(mi_cd)