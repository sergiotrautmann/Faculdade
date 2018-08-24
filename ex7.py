arquivo = open('abastecimento.txt','r+')
conteudo = arquivo.readlines()
km = input('Qual a quilometragem do veiculo na hora do abastecimento?:')
quantidade = input('Qual a quantidade de combustivel abastecido?:')
valor = input('Qual o valor pago?:')
conteudo.append('quilometro: \n' + km)
conteudo.append('\nquantidade: \n' + quantidade)
conteudo.append('\nvalor: \n'  + valor +'\n')
arquivo = open('abastecimento.txt', 'r+')
arquivo.writelines(conteudo)

arquivo.close()


arquivo = open('abastecimento.txt','r+')
conteudo = arquivo.readlines()
km = input('Qual a quilometragem do veiculo na hora do abastecimento?:')
quantidade = input('Qual a quantidade de combustivel abastecido?:')
valor = input('Qual o valor pago?:')
c = km + ';' + quantidade + ';' + valor +'\n'
conteudo.append(c)
arquivo = open('abastecimento.txt', 'r+')
arquivo.writelines(conteudo )
arquivo.close()
arquivo = open('abastecimento.txt','r')
for linha in arquivo:
    l =linha.split(';')
    tkm = float(l[0])
    tqt = float(l[1])
    tvl = float(l[2])
    tkm1 = 0
    tqt1 = 0
    tvl1 = 0
    tkm1 += + tkm
    tqt1 += + tqt
    tvl1 += + tvl
    media = 0
    media += tkm1/ tqt1
    print('a media de consumo por km é', media)
    print('o total gasto em combustível foi: R$',tvl1)
