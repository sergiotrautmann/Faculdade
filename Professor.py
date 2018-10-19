from pessoa import Pessoa
class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, salario, curso, materia):
        # referencia a caracteristicas da classe mae
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.salario = salario
        self.curso = curso
        self.materia = materia

    def __str__(self):
        return f'Nome: {super().__str__()}\nMatricula: {self.matricula}\nSalario: {self.salario}\nCurso: {self.curso}\nMateria: {self.materia}'