def maiusculo(palavra):
    if palavra.lower() == palavra:
        return False
    else:
        return True
print(maiusculo('Certo'))
print(maiusculo('errado'))
print(maiusculo('nãoSei'))
print(maiusculo('podEseR'))