cliente = {'nombre':'Pedro', 'apellido':'Petit', 'altura':1.75, 'peso':88}
consulta = cliente['apellido']
print(consulta)

dic = {'nombre':'Joaquin', 'hobbys':{'deporte':'beisbol','estudios':'programación'}, 'paises':['Venezuela','Panamá','Colombia']}
print(dic['paises'][2])
print(dic['hobbys']['estudios'].upper())

dic['edad'] = 34
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())