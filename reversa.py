def reversa(l):
    lista = [0]*len(l)
    for i in range(0,len(l)):
        lista[i] = l[len(l)-i-1]
    return lista

print(reversa([1,2,3,4]))