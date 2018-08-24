def mdc(n1, n2):
    if n2 == 0:
        return n1
    else:
        return mdc(n2, n1 % n2)
n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
print(mdc(n1, n2))
