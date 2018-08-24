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


