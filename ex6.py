def is_triangle(n1,n2,n3):
    if n1 > n2 + n3:
        return False
    elif n2 > n1 + n3:
        return False
    elif n3 > n1 + n2:
        return False
    else:
        return True

numero1 = float(input('Digite o primeiro número:'))
numero2 = float(input('Digite o segundo número:'))
numero3 = float(input('Digite o terceiro número:'))
print(is_triangle(numero1, numero2, numero3))
