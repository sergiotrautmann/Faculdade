from carro import Veiculo
from concessionaria import Concessionaria
from comprador import Comprador
from vendedor import Vendedor
v12 = Concessionaria('V12 MOTORS')

print(v12.nome)

up = Veiculo('UP', 2018, 'novo', 20000)
v12.add_carro(up)

print(v12.get_carros()[0].get_modelo())

mobi = Veiculo('MOBI', 2017, 'USADO', 17000)
v12.add_carro(mobi)
print(v12.get_carros()[1].get_modelo())
for carro in v12.get_carros():
    print(carro.get_modelo())

comprador1 = Comprador('Sergio', '045.483.731-36')
comprador2 = Comprador('Patrick', '045.483.731-37')
vendedor1 = Vendedor('Rafael', '000.000.000-00', 9156)
up.venda(comprador1, vendedor1)
print(up.data_da_venda)
print(up.comprador.nome)
print(up.vendedor.nome)
