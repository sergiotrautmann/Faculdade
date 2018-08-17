lista = [7, 2, 12, 4, 8]
ct = 0
while True:
    for x in range(4):
        ct = ct + 1
        if lista[x] > lista[x+1]:
                temp = lista[x]
                lista[x] = lista[x+1]
                lista[x+1] = temp
                print(lista)
                print("Foram feitos", ct, "testes.")