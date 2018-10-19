class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.idade

    #sobrescerver o metodo str
    def __str__(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}'