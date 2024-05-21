def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    
    return total
print(suma(x=3,y=5,z=20))

def prueba(num1, num2, *args, **kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

args = [500,345,234]
kwargs = {'1': 'uno','2':'dos', '3': 'tres', '4':'cuatro' }
prueba(500,1,53,24,25,6,34,x=3,y=5,z=20)
prueba(500,1,*args,**kwargs)