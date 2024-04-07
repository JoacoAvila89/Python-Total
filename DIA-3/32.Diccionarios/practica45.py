"""Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Karen

apellido: Jurgens

edad: 36

ocupacion: Editora

pais: Colombia"""

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic["ocupacion"]= 'Editora'
mi_dic["edad"]= 36
mi_dic['pais'] = "Colombia"
print(mi_dic)
