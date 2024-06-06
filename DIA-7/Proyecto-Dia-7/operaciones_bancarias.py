from random import randint
class Persona:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, nro_cuenta, balance) -> None:
        super().__init__(nombre, apellido)
        self.nro_cuenta = nro_cuenta
        self.balance = balance

    def __str__(self) -> str:
        return f" -Nombre del cliente: {self.nombre}\n -Apellido: {self.apellido}\n -Nro de cuenta: {self.nro_cuenta}\n -Balance: {self.balance}"
    
    def depositar(self):
        monto = float(input("Cuanto dinero desea depositar: "))
        self.balance += monto
        return self.balance

    def retirar(self):
        monto = float(input("Cuanto dinero desea retirar: "))
        if monto > self.balance:
            print("No puede retirar un monto mayor al disponible")
        else:
            self.balance -= monto
        return self.balance
        
def crear_cliente():
    nombre = input("Cual es su nombre: ")
    apellido = input("Cual es su apellido: ")
    nro_cuenta = randint(1, 5000000)
    balance = 0.0
    cliente = Cliente(nombre,apellido,nro_cuenta,balance)

    return cliente

def inicio():   
    nuevo_cliente = crear_cliente()
    finalizar = False
    while not finalizar:

        eleccion_menu = 'x'
        while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,4):
            print("Elige una opcion:")
            print('''
            [1] - Depositar
            [2] - Retirar
            [3] - Salir''')
            eleccion_menu = input("Elige una opcion: ")
   
        if eleccion_menu == '1':
            nuevo_cliente.depositar()
            print(f"Número de cuenta: {nuevo_cliente.nro_cuenta}\nFondos disponibles: {nuevo_cliente.balance}")
        elif eleccion_menu == '2':
            nuevo_cliente.retirar()
            print(f"Número de cuenta: {nuevo_cliente.nro_cuenta}\nFondos disponibles: {nuevo_cliente.balance}")
        else:
            finalizar = True
        
inicio()
