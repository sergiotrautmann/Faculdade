fruta = 'banana'
print('foram contadas:', fruta.count('a'), 'letras a')

tipo = 'universidade'
print('foram contadas:', tipo.count('e'), 'letras e')

def maiusculo(palavra):
    if palavra.lower() == palavra:
        return False
    else:
        return True
print(maiusculo('podEseR'))


frase1 = 'Hoje está chovendo desde muito cedo'
Letras_proibidas1 = ['o', 'd', 't']
for letra1 in Letras_proibidas1:
    print('foram contadas:', frase1.count(letra1), 'letras', letra1)


frase2 = 'Amanha vai ser outro dia'
Letras_proibidas2 = ['m', 'p', 'q', 'a']
for letra2 in Letras_proibidas2:
    print('foram contadas:', frase2.count(letra2), 'letras', letra2)


numeros = [[1, 2], [23, 5, 9, 10], [1, 8, 16]]
a = sum(numeros[0])
b= sum(numeros[1])
c=sum(numeros[2])
print(a+b+c)


def mdc(n1, n2):
    if n2 ==0:
        return n1
    else:
        return mdc (n2, n1 % n2)
n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
print(mdc(n1, n2))

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
print(is_triangle(numero1,numero2,numero3))
