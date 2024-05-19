"""
Python set isdisjoint() function check whether the two sets are disjoint or not, if it is disjoint then it 
returns True otherwise it will return False. Two sets are said to be disjoint when their intersection is null. 
"""
#Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)