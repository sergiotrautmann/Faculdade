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
            self.comprador = comprador
            self.vendedor = vendedor
            self.disponivel = False
            print('O carro foi vendido no dia:',self.data_da_venda, ',', 'Comprador por:',self.comprador.nome, 'e', "Vendido por", self.vendedor.nome)

    def get_modelo(self):
        return self.modelo

