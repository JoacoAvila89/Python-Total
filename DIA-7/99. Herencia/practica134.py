"""
Práctica Herencia 2
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase,
Perro, que herede de la primera sus atributos.
"""
class Mascota:
    def __init__(self,edad,nombre,cantidasd_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidasd_patas

class Perro(Mascota):
    pass