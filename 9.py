from datetime import date
class Veiculo:
    def __init__(self, modelo, ano, estado, preco):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
        self.preco = preco
        self.disponivel = True
        self.data_da_venda = None
        self.comprador = None
        self.vendedor = None

    def disponibilidade(self):
        return self.disponivel

    def venda(self, comprador, vendedor):
        if self.disponivel:
            self.data_da_venda = date.today()
            self.comprador = comprador.nome
            self.vendedor = vendedor.nome
            self.disponivel = False
            print('O carro foi vendido no dia:',self.data_da_venda,',', 'Comprador por:',comprador.nome, 'e',"Vendido por", vendedor.nome)


class Comprador:
    def __init__(self, nome):
        self.nome = nome


class Vendedor:
    def __init__(self, nome):
        self.nome = nome




carro1 = Veiculo('Corolla', 2006, 'semi-novo', 20.000)
comprador1 = Comprador('Sergio')
vendedor1 = Vendedor('Rafael')
carro1.venda(comprador1, vendedor1)
print(carro1.data_da_venda)
print(carro1.comprador)
print(carro1.vendedor)