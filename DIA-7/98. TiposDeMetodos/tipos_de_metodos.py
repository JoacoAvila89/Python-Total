class Pajaro:
    alas = True

    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print("pio, mi color es {}".format(self.color))
    
  
    def volar(self,metros):
        print(f"El pajaro ha volado {metros} metros")
        #Los metodos de instancia pueden llamar a otros metodos
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f"Ahora el pajaro es de corlor {self.color}")

    #metodos de clase
    @classmethod
    def poner_huevo(cls,cantidad):
        print(f"puso {cantidad} huevos")
        cls.alas = False
        print(Pajaro.alas)
    
    #métodos estaticos
    @staticmethod
    def mirar():
        print("El pajaro mira")

piolin = Pajaro("Amarillo", "Canario")
piolin.piar()
piolin.volar(500)
piolin.alas = False
print(piolin.alas)

Pajaro.poner_huevo(4)

Pajaro.mirar()