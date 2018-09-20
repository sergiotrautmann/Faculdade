def media(n1, n2, n3):
    m = (n1 + n2 + n3)/3
    return  calcular_mencao(m)

def calcular_mencao(m):
    if m >= 9:
        mencao = 'SS'
    elif m >= 7:
        mencao = 'MS'
    elif m >= 5:
        mencao = 'MM'
    elif m >= 3:
        mencao = 'MI'
    elif m > 0:
        mencao = 'II'
    else:
        mencao = 'SR'
    return mencao

n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))

print(media(n1, n2, n3))