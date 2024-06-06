class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite un sonido  ")

class Pajaro(Animal):

    def __init__(self,edad, color,altura_vuelo):
        #Cuando tienes muchos atrubutos puedes usar super, y ya te trae los atributos heredados
        super().__init__(color,edad)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Ahora el pajaro dice pio ")
    
    def volar(self,metros):
        print(f"Este pajaro vuela {metros} metros")


piolin = Pajaro(3,"Amarillo",70)
piolin.nacer()
piolin.hablar()
piolin.volar(50)

otro_animal = Animal(10,"Verde")
otro_animal.hablar()


#Herencia Multiple

class Padre:
    def hablar(self):
        print("Hola, yo hablo ingles")

class Madre:
    def reir(self):
        print("ja ja ja")
    
    def hablar(self):
        print("Hola, yo hablo español")

class Hijo(Padre,Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.reir()
#Como hijo hereda de padre y madre aca imprime el primer metodo hablar, porque dentro de los parametros hijo hereda primero de 
# de padre y luego de madre --> class Hijo(Padre,Madre). Si fuese asi class Hijo(Madre,Padre) imprime que habla español
mi_nieto.hablar()
