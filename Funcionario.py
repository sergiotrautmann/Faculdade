from pessoa import Pessoa
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, salario, setor):
#referencia a caracteristicas da classe mae
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.setor = setor
    def __str__(self):
        return f'Nome: {super().__str__()}\nMatricula: {self.matricula}\nSalario: {self.salario}\nSetor: {self.setor}'