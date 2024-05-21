nombres = ['Liz','Delvalle', 'Gregorio', 'Luisa', 'Nelson', 'Nina']
edades = [30,58,60,77,34,66]

combinados = list(zip(nombres,edades))
print(combinados)

for nombre,edad in combinados:
    print(f"{nombre} tiene {edad} años")