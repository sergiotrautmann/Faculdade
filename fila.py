ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print('Tamanho da fila', len(fila))
    print('Fila atual:', fila)

    operacao = input('Operação A, C, ou S:')
    if operacao == 'A':
        morto = fila.pop(0)
        print('Matei o', morto)
    if operacao == 'C':
        ultimo = ultimo + 1
        fila.append(ultimo)
    if operacao == 'S':
        break

    else:
        print('Digite A, C ou S:')
