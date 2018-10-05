class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def get_nome(self):
        return self.nome

    def get_carros(self):
        return self.carros

    def add_carro(self, carro):
        self.carros.append(carro)
