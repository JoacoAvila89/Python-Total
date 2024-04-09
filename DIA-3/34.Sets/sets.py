mi_set = set((1,2,3,4,5))

print(len(mi_set))
print(2 in mi_set)

s1 ={1,2,3}
s2 ={3,4,5}
s3 = s1.union(s2)
s3.add(6)
s3.remove(5)

#Elimina un elemento aleatorio
s3.pop()
print(s3)