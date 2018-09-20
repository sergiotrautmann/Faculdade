
class Paciente:
    def __init__(self, nome, sexo, idade, especialidade):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.especialidade = especialidade

paciente1 = Paciente('nome1', 'masculino', 40, 'odontologia')
paciente2 = Paciente('nome2', 'masculino', 30, 'asdasdas')