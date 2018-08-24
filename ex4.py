def soma_completa(numeros):
    soma =0
    for sub_lista in numeros:
        for item in sub_lista:
            soma += item
    return soma
numeros = [[1, 2], [23, 5, 9, 10], [1, 8, 16]]
print(soma_completa(numeros))