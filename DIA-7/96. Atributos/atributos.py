class Pajaro:
    #
    alas = True

    """def __init__(self,parametro):
        self.atributo = parametro"""
    def __init__(self,color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("Negro", "Carpintero")

print(f"Mi pajaro es de color {mi_pajaro.color} y es de la especie {mi_pajaro.especie}")

print(Pajaro.alas)
print(mi_pajaro.alas)