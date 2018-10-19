from pessoa import Pessoa
class Estudante(Pessoa):
    def __init__(self, nome, cpf, idade, RA , curso, semestre):
        # referencia a caracteristicas da classe mae
        super().__init__(nome, cpf, idade)
        self.RA = RA
        self.curso = curso
        self.semestre = semestre

    def __str__(self):
        return f'Nome: {super().__str__()}\nRA: {self.RA}\nCurso: {self.curso}\nSemestre: {self.semestre}'