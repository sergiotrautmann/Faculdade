def calcular_mencao(n1):
    if n1 >= 9:
        mencao = 'SS'
    elif n1 >= 7:
        mencao = 'MS'
    elif n1 >= 5:
        mencao = 'MM'
    elif n1 >= 3:
        mencao = 'MI'
    elif n1 > 0:
        mencao = 'II'
    else:
        mencao = 'SR'
    return mencao

n1 = float(input('Digite o primeiro número:'))


print(calcular_mencao(n1))