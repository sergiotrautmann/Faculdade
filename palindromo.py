def palindromo(palavra):
    for letra in palavra:
        a = letra

    for letra1 in palavra[::-1]:
        b = letra1

    if a == b:
        print('É palíndromo')
    else:
        print('Não é palindromo')

palindromo('aibofobia')


def is_palindromo(palavra):
    if len(palavra) > 1:
        for x in range(0, int(len(palavra) / 2)):
            if palavra[x] != palavra[(len(palavra) - 1) - x]:
                return False
        return True


print(is_palindromo('osso'))

def palindromo(palavra):
    if len(palavra) < 2:
        return True
    elif palavra[0] != palavra[-1]:
        return False
    else:
        return palindromo(palavra[1:len(palavra)-1])

print(palindromo('osso'))