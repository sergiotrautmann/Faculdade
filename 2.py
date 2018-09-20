def alistamento(sexo, idade):
    if sexo == 'Feminino':
        return  False
    elif sexo == 'Masculino':
        if 27 >= idade >= 18:
            return True
        else:
            return False


print(alistamento('Masculino',18))