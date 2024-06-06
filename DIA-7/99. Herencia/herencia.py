class Animal:
    def __init__(self,edad, color):
        self.edad = edad
        self.color = color

    def nacer():
        print("Este animal ha nacido")

class Pajaro(Animal):
    def volar(metros):
        print(f"Este pajaro vuela {metros} metros")

condorito = Pajaro
condorito.nacer()

piolin = Pajaro(2,"Amarillo")
print(piolin.color)