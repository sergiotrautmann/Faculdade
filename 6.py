lista = [0,4,9,101,15,10]

def maior_numero(lista):
    b =True
    while b:
        l = len(lista)
        for x in range(l-1):
            if lista[x] > lista[x+1]:
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
                b =False
        return lista[l-1]
print(maior_numero(lista))


